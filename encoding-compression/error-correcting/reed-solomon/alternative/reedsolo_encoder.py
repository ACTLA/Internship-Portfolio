import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QFileDialog,
    QTextEdit, QWidget, QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor
import reedsolo


class RSApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rs = reedsolo.RSCodec(32)  # RS-код с 32 контрольными символами
        self.initUI()
        self.data = None
        self.encoded_data = None

    def initUI(self):
        self.setWindowTitle("Код Рида-Соломона")
        self.setGeometry(100, 100, 1200, 600)

        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)

        # Верхняя панель с кнопками
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.load_button = QPushButton("Загрузить файл")
        self.load_button.clicked.connect(self.load_file)
        button_layout.addWidget(self.load_button)

        self.encode_button = QPushButton("Кодировать")
        self.encode_button.clicked.connect(self.encode_text)
        button_layout.addWidget(self.encode_button)

        self.decode_button = QPushButton("Декодировать")
        self.decode_button.clicked.connect(self.decode_text)
        button_layout.addWidget(self.decode_button)

        # Текстовые поля
        self.file_text_label = QLabel("Считанный текст:")
        layout.addWidget(self.file_text_label)
        self.file_text_edit = QTextEdit()
        layout.addWidget(self.file_text_edit)

        self.encoded_bits_label = QLabel("Закодированные биты:")
        layout.addWidget(self.encoded_bits_label)
        self.encoded_bits_text = QTextEdit()
        layout.addWidget(self.encoded_bits_text)

        self.corrupted_bits_label = QLabel("Закодированные биты с ошибками:")
        layout.addWidget(self.corrupted_bits_label)
        self.corrupted_bits_text = QTextEdit()
        layout.addWidget(self.corrupted_bits_text)

        self.decoded_text_label = QLabel("Декодированный текст:")
        layout.addWidget(self.decoded_text_label)
        self.decoded_text_edit = QTextEdit()
        layout.addWidget(self.decoded_text_edit)

        self.error_report_label = QLabel("Отчет об ошибках:")
        layout.addWidget(self.error_report_label)
        self.error_report_text = QTextEdit()
        self.error_report_text.setReadOnly(True)
        layout.addWidget(self.error_report_text)

    def load_file(self):
        """Загрузка файла и интерпретация содержимого как текста."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выбрать файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read().strip()
                    self.data = content
                    self.file_text_edit.setPlainText(self.data)
            except Exception as e:
                QMessageBox.critical(
                    self, "Ошибка", f"Не удалось прочитать файл: {e}")
        else:
            QMessageBox.warning(self, "Ошибка", "Файл не выбран.")

    def encode_text(self):
        """Кодирование считанного текста."""
        text = self.file_text_edit.toPlainText().strip()
        if not text:
            QMessageBox.warning(
                self, "Ошибка", "Сначала загрузите файл с текстом.")
            return
        try:
            # Преобразуем текст в байты
            bytes_data = text.encode("utf-8")
            self.encoded_data = self.rs.encode(bytes_data)
            # Преобразуем закодированные байты обратно в биты
            encoded_bits = ''.join(format(byte, '08b')
                                   for byte in self.encoded_data)
            self.encoded_bits_text.setPlainText(encoded_bits)
            self.corrupted_bits_text.setPlainText(
                encoded_bits)  # Копируем в поле с ошибками
        except Exception as e:
            QMessageBox.critical(self, "Ошибка кодирования", f"{e}")

    def decode_text(self):
        """Декодирование битов и исправление ошибок с подсветкой."""
        bits = self.corrupted_bits_text.toPlainText().strip()
        if not bits:
            QMessageBox.warning(
                self, "Ошибка", "Введите закодированные биты с ошибками.")
            return
        try:
            # Преобразуем биты в байты
            corrupted_bytes = bytes(int(bits[i:i + 8], 2)
                                    for i in range(0, len(bits), 8))
            decoded_data, _, errata_pos = self.rs.decode(corrupted_bytes)
            # Преобразуем декодированные байты обратно в текст
            decoded_text = decoded_data.decode("utf-8")
            self.decoded_text_edit.setPlainText(decoded_text)

            # Подсветка ошибок
            self.highlight_errors(errata_pos)

            # Вывод отчета об ошибках
            self.error_report_text.clear()
            if errata_pos:
                self.error_report_text.append(
                    "Ошибки обнаружены и исправлены:")
                for pos in errata_pos:
                    self.error_report_text.append(f"Позиция: {pos}")
            else:
                self.error_report_text.append("Ошибок не обнаружено.")
        except reedsolo.ReedSolomonError as e:
            QMessageBox.critical(self, "Ошибка декодирования", f"{e}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"{e}")

    def highlight_errors(self, errata_pos):
        """Подсветка исправленных ошибок в закодированном тексте с ошибками."""
        if not errata_pos:
            return

        cursor = self.corrupted_bits_text.textCursor()
        format_error = QTextCharFormat()
        # Подсветка исправлений желтым
        format_error.setBackground(QColor("yellow"))

        self.corrupted_bits_text.setTextCursor(cursor)
        for pos in errata_pos:
            # Находим позицию байта и подсвечиваем соответствующие 8 бит
            bit_start = pos * 8
            for i in range(8):
                cursor.setPosition(bit_start + i)
                cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor)
                cursor.mergeCharFormat(format_error)


# Запуск приложения
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RSApp()
    window.show()
    sys.exit(app.exec_())
