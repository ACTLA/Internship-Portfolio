import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QTextEdit, QLabel, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QTextCharFormat, QTextCursor


def text_to_bits(text):
    return ''.join(f'{ord(c):08b}' for c in text)


def bits_to_text(bits):
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))


def hamming_encode(data):
    m = len(data)
    r = 1
    while (2 ** r - 1) < m + r:
        r += 1

    n = m + r
    encoded = ['0'] * n

    j = 0
    for i in range(1, n + 1):
        if i & (i - 1) == 0:  # проверка, является ли i степенью двойки
            encoded[i - 1] = '0'
        else:
            encoded[i - 1] = data[j]
            j += 1

    for i in range(r):
        pos = 2 ** i
        count = 0
        for j in range(1, n + 1):
            if j & pos:
                if encoded[j - 1] == '1':
                    count += 1
        encoded[pos - 1] = str(count % 2)

    return ''.join(encoded)


def hamming_decode(data):
    n = len(data)
    r = 0
    while (2 ** r - 1) < n:
        r += 1

    error_pos = 0
    for i in range(r):
        pos = 2 ** i
        count = 0
        for j in range(1, n + 1):
            if j & pos:
                if data[j - 1] == '1':
                    count += 1
        error_pos += pos * (count % 2)

    if error_pos == 0:
        return data, None
    else:
        corrected_data = list(data)
        corrected_data[error_pos -
                       1] = '0' if corrected_data[error_pos - 1] == '1' else '1'
        return ''.join(corrected_data), error_pos


def encode_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    bits = text_to_bits(text)
    encoded_bits = []
    for i in range(0, len(bits), 4):
        block = bits[i:i+4]
        encoded_block = hamming_encode(block)
        encoded_bits.append(encoded_block)

    with open(output_file, 'w') as f:
        for block in encoded_bits:
            f.write(block + '\n')

    return encoded_bits


def decode_file(input_file, output_file):
    with open(input_file, 'r') as f:
        encoded_bits = f.read().strip().split('\n')

    decoded_text = ''
    error_report = []
    corrected_blocks = []
    for i, block in enumerate(encoded_bits):
        decoded_block, error_pos = hamming_decode(block)
        if error_pos:
            error_report.append(f'Ошибка в блоке {i + 1}, бит {error_pos}')
        decoded_bits = ''
        for j in range(1, len(decoded_block) + 1):
            if j & (j - 1) != 0:
                decoded_bits += decoded_block[j - 1]
        decoded_text += decoded_bits
        corrected_blocks.append(decoded_block)

    text = bits_to_text(decoded_text)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

    return error_report, corrected_blocks


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Кодировщик/Декодировщик Хэмминга')
        self.setGeometry(100, 100, 600, 600)

        layout = QVBoxLayout()

        self.encode_button = QPushButton('Закодировать файл', self)
        self.encode_button.clicked.connect(self.encode_file_dialog)
        layout.addWidget(self.encode_button)

        self.decode_button = QPushButton('Декодировать файл', self)
        self.decode_button.clicked.connect(self.decode_file_dialog)
        layout.addWidget(self.decode_button)

        self.clear_buttons_layout = QVBoxLayout()
        self.clear_error_report_button = QPushButton(
            'Очистить отчет об ошибках', self)
        self.clear_error_report_button.clicked.connect(self.clear_error_report)
        self.clear_buttons_layout.addWidget(self.clear_error_report_button)

        self.clear_encoded_text_button = QPushButton(
            'Очистить закодированный текст', self)
        self.clear_encoded_text_button.clicked.connect(self.clear_encoded_text)
        self.clear_buttons_layout.addWidget(self.clear_encoded_text_button)

        self.clear_corrected_text_button = QPushButton(
            'Очистить исправленный текст', self)
        self.clear_corrected_text_button.clicked.connect(
            self.clear_corrected_text)
        self.clear_buttons_layout.addWidget(self.clear_corrected_text_button)

        layout.addLayout(self.clear_buttons_layout)

        self.error_report = QTextEdit(self)
        self.error_report.setReadOnly(True)
        self.error_report.setFixedHeight(100)
        layout.addWidget(self.error_report)

        self.encoded_text = QTextEdit(self)
        self.encoded_text.setReadOnly(True)
        layout.addWidget(self.encoded_text)

        self.corrected_text = QTextEdit(self)
        self.corrected_text.setReadOnly(True)
        layout.addWidget(self.corrected_text)

        self.setLayout(layout)

    def encode_file_dialog(self):
        input_file, _ = QFileDialog.getOpenFileName(
            self, 'Выберите файл для кодирования', '', 'Текстовые файлы (*.txt)')
        if input_file:
            output_file = os.path.splitext(input_file)[0] + '_encoded.txt'
            encoded_blocks = encode_file(input_file, output_file)
            self.encoded_text.clear()
            for i, block in enumerate(encoded_blocks):
                self.encoded_text.append(f'{i + 1}: {block}')
            QMessageBox.information(
                self, 'Информация', f'Файл закодирован: {output_file}')

    def decode_file_dialog(self):
        input_file, _ = QFileDialog.getOpenFileName(
            self, 'Выберите файл для декодирования', '', 'Текстовые файлы (*.txt)')
        if input_file:
            output_file = os.path.splitext(input_file)[0] + '_decoded.txt'
            error_report, corrected_blocks = decode_file(
                input_file, output_file)
            self.error_report.clear()
            self.corrected_text.clear()
            for error in error_report:
                self.error_report.append(error)
            for i, block in enumerate(corrected_blocks):
                format = QTextCharFormat()
                if any(char in block for char in '1'):
                    format.setBackground(QColor('green'))
                if '11' in block:
                    format.setBackground(QColor('yellow'))
                self.corrected_text.append(f'{i + 1}: {block}')
                cursor = self.corrected_text.textCursor()
                cursor.setPosition(self.corrected_text.textCursor(
                ).position() - len(block) - 2, QTextCursor.MoveAnchor)
                cursor.movePosition(QTextCursor.EndOfBlock,
                                    QTextCursor.KeepAnchor)
                cursor.mergeCharFormat(format)
            QMessageBox.information(
                self, 'Информация', f'Файл декодирован: {output_file}')

    def clear_error_report(self):
        self.error_report.clear()

    def clear_encoded_text(self):
        self.encoded_text.clear()

    def clear_corrected_text(self):
        self.corrected_text.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
