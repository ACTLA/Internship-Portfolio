import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QFileDialog,
    QVBoxLayout, QWidget, QComboBox, QMessageBox
)
import chardet


class EncodingConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Конвертер кодировок текста")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Выберите файл для обработки")
        layout.addWidget(self.label)

        self.choose_file_button = QPushButton("Выбрать файл")
        self.choose_file_button.clicked.connect(self.choose_file)
        layout.addWidget(self.choose_file_button)

        self.encoding_label = QLabel("Определённая кодировка: Не выбрано")
        layout.addWidget(self.encoding_label)

        self.target_encoding_label = QLabel("Целевая кодировка:")
        layout.addWidget(self.target_encoding_label)

        self.encoding_selector = QComboBox()
        self.encoding_selector.addItems(
            ["CP866", "CP1251", "CP10007 (MacCyrillic)", "ISO-8859-5"]
        )
        layout.addWidget(self.encoding_selector)

        self.convert_button = QPushButton("Конвертировать")
        self.convert_button.clicked.connect(self.convert_encoding)
        layout.addWidget(self.convert_button)

        self.status_label = QLabel("")
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.file_path = None
        self.current_encoding = None

    def choose_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self, "Выберите текстовый файл", "", "Текстовые файлы (*.txt)"
        )

        if file_path:
            self.file_path = file_path
            self.label.setText(f"Файл: {file_path}")
            self.detect_encoding()

    def detect_encoding(self):
        if not self.file_path:
            return

        try:
            with open(self.file_path, "rb") as f:
                raw_data = f.read()
                result = chardet.detect(raw_data)
                self.current_encoding = result['encoding']
                self.encoding_label.setText(f"Определённая кодировка: {
                                            self.current_encoding}")
        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка", f"Не удалось определить кодировку: {e}"
            )

    def convert_encoding(self):
        if not self.file_path:
            QMessageBox.warning(self, "Ошибка", "Сначала выберите файл!")
            return

        if not self.current_encoding:
            QMessageBox.warning(
                self, "Ошибка", "Кодировка файла не определена!"
            )
            return

        target_encoding = self.encoding_selector.currentText()

        # Определяем внутреннюю кодировку, но сохраняем оригинальное имя
        if "CP10007" in target_encoding:
            internal_encoding = "mac_cyrillic"  # Используется для обработки
            display_encoding = "CP10007"  # Отображается в имени файла
        else:
            internal_encoding = target_encoding
            display_encoding = target_encoding

        try:
            # Читаем исходный файл с текущей кодировкой
            with open(self.file_path, "r", encoding=self.current_encoding) as f:
                content = f.read()

            # Сохраняем файл с целевой кодировкой
            output_file = self.file_path.rsplit(
                ".", 1)[0] + f"_{display_encoding}.txt"
            with open(output_file, "w", encoding=internal_encoding) as f:
                f.write(content)

            self.status_label.setText(f"Файл сохранён: {output_file}")
            QMessageBox.information(
                self,
                "Успех",
                f"Файл успешно конвертирован в {
                    target_encoding} и сохранён как {output_file}"
            )
        except Exception as e:
            QMessageBox.critical(
                self, "Ошибка", f"Не удалось выполнить конвертацию: {e}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EncodingConverter()
    window.show()
    sys.exit(app.exec())
