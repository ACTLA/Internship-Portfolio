import sys
import os
import struct
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QFileDialog, QMessageBox

# Реализация алгоритма LZ78


def compress_lz78(text: str) -> list:
    dictionary = {0: ""}
    result = []
    current_string = ""
    index = 1

    for char in text:
        new_string = current_string + char
        if new_string in dictionary.values():
            current_string = new_string
        else:
            for k, v in dictionary.items():
                if v == current_string:
                    result.append((k, char))
                    break
            dictionary[index] = new_string
            index += 1
            current_string = ""

    if current_string != "":
        for k, v in dictionary.items():
            if v == current_string:
                result.append((k, ""))
                break

    return result


def decompress_lz78(encoded: list) -> str:
    dictionary = {0: ""}
    result = ""
    index = 1

    for pair in encoded:
        index_part, char_part = pair
        current_string = dictionary[index_part] + \
            (char_part if char_part else "")
        result += current_string
        dictionary[index] = current_string
        index += 1

    return result

# Функции для сохранения и загрузки бинарных данных


def save_compressed(compressed: list, file_name: str):
    with open(file_name, 'wb') as file:
        for index, char in compressed:
            if char:
                file.write(struct.pack('Hc', index, char.encode('utf-8')))
            else:
                file.write(struct.pack('Hc', index, b'\0'))


def load_compressed(file_name: str) -> list:
    compressed = []
    with open(file_name, 'rb') as file:
        while True:
            byte_data = file.read(3)
            if not byte_data:
                break
            index, char = struct.unpack('Hc', byte_data)
            compressed.append(
                (index, char.decode('utf-8') if char != b'\0' else ""))
    return compressed

# Реализация GUI на PyQt


class LZ78App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Сжатие LZ78')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Input Text
        self.input_label = QLabel('Входной текст:')
        self.input_text = QTextEdit()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)

        # Buttons for file operations
        file_button_layout = QHBoxLayout()
        self.load_button = QPushButton('Загрузить .txt файл')
        self.load_button.clicked.connect(self.load_file)
        self.save_compressed_button = QPushButton('Сохранить сжатый файл')
        self.save_compressed_button.clicked.connect(self.save_compressed_file)
        self.load_compressed_button = QPushButton('Загрузить сжатый файл')
        self.load_compressed_button.clicked.connect(self.load_compressed_file)
        self.save_output_button = QPushButton('Сохранить разжатый файл')
        self.save_output_button.clicked.connect(self.save_output_file)
        file_button_layout.addWidget(self.load_button)
        file_button_layout.addWidget(self.save_compressed_button)
        file_button_layout.addWidget(self.load_compressed_button)
        file_button_layout.addWidget(self.save_output_button)
        layout.addLayout(file_button_layout)

        # Buttons for compression and decompression
        button_layout = QHBoxLayout()
        self.compress_button = QPushButton('Сжать')
        self.compress_button.clicked.connect(self.compress_text)
        self.decompress_button = QPushButton('Разжать')
        self.decompress_button.clicked.connect(self.decompress_text)
        button_layout.addWidget(self.compress_button)
        button_layout.addWidget(self.decompress_button)
        layout.addLayout(button_layout)

        # Output Text
        self.output_label = QLabel('Выходной текст:')
        self.output_text = QTextEdit()
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)

        self.setLayout(layout)

    def load_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Загрузить .txt файл", "", "Текстовые файлы (*.txt);;Все файлы (*)", options=options)
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.input_text.setPlainText(file.read())

    def save_compressed_file(self):
        compressed = self.output_text.toPlainText()
        try:
            compressed_list = eval(compressed)
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(
                self, "Сохранить сжатый файл", "", "Бинарные файлы (*.bin);;Все файлы (*)", options=options)
            if file_name:
                save_compressed(compressed_list, file_name)
        except Exception as e:
            self.show_message(
                f"Неверный формат входных данных. Пожалуйста, убедитесь, что введен корректный список кортежей. Ошибка: {e}")

    def load_compressed_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Загрузить сжатый файл", "", "Бинарные файлы (*.bin);;Все файлы (*)", options=options)
        if file_name:
            compressed_list = load_compressed(file_name)
            self.input_text.setPlainText(
                str(compressed_list))  # Загружаем в input_text
            self.output_text.setPlainText("")  # Очищаем output_text

    def save_output_file(self):
        output_text = self.output_text.toPlainText()
        if not output_text:
            self.show_message(
                "Выходной текст пуст. Пожалуйста, введите текст.")
            return
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Сохранить выходной текст в .txt файл", "", "Текстовые файлы (*.txt);;Все файлы (*)", options=options)
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(output_text)

    def compress_text(self):
        input_text = self.input_text.toPlainText()
        if not input_text:
            self.show_message("Входной текст пуст. Пожалуйста, введите текст.")
            return
        compressed = compress_lz78(input_text)
        self.output_text.setPlainText(str(compressed))

    def decompress_text(self):
        input_text = self.input_text.toPlainText()  # Загружаем из input_text
        if not input_text:
            self.show_message("Входной текст пуст. Пожалуйста, введите текст.")
            return
        try:
            compressed = eval(input_text)
            decompressed = decompress_lz78(compressed)
            self.output_text.setPlainText(decompressed)
        except Exception as e:
            self.show_message(
                f"Неверный формат входных данных. Пожалуйста, убедитесь, что введен корректный список кортежей. Ошибка: {e}")

    def show_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText(message)
        msg_box.setWindowTitle("Предупреждение")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LZ78App()
    ex.show()
    sys.exit(app.exec_())
