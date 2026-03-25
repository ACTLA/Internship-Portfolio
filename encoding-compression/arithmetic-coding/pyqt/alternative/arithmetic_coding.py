import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QLineEdit, QFormLayout, QTextBrowser
from PyQt5.QtGui import QIntValidator


def cumulative_probabilities(frequencies):
    total = sum(frequencies.values())
    cumulative = 0.0
    probabilities = {}
    for char, freq in sorted(frequencies.items()):
        probabilities[char] = (cumulative, cumulative + freq / total)
        cumulative += freq / total
    return probabilities


def encode(text, probabilities):
    low, high = 0.0, 1.0
    process = []
    for char in text:
        process.append(f"Символ: {char}, Новый интервал: [{
                       low + (high - low) * probabilities[char][0]:.10f}, {low + (high - low) * probabilities[char][1]:.10f})")
        low, high = low + \
            (high - low) * probabilities[char][0], low + \
            (high - low) * probabilities[char][1]
    code = (low + high) / 2.0
    return code, process


def decode(code, probabilities, length):
    text = []
    low, high = 0.0, 1.0
    process = []
    for _ in range(length):
        for char, (low_prob, high_prob) in probabilities.items():
            if low <= code < high:
                if low_prob <= (code - low) / (high - low) < high_prob:
                    text.append(f"Символ: {char}, Новый интервал: [{
                                low + (high - low) * low_prob:.10f}, {low + (high - low) * high_prob:.10f})")
                    text.append(char)
                    low, high = low + (high - low) * \
                        low_prob, low + (high - low) * high_prob
                    break
    return ''.join(text[1::2]), text


class ArithmeticCodingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Арифметическое Кодирование')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        form_layout = QFormLayout()
        self.input_text = QTextEdit()
        self.encoder_output = QTextEdit()
        self.decoder_output = QTextEdit()
        self.length_input = QLineEdit()
        self.length_input.setValidator(QIntValidator())
        self.frequencies_output = QTextEdit()
        self.probabilities_output = QTextEdit()
        self.encode_process_output = QTextEdit()
        self.decode_process_output = QTextEdit()

        form_layout.addRow(QLabel('Исходный текст:'), self.input_text)
        form_layout.addRow(QLabel('Кодированный текст:'), self.encoder_output)
        form_layout.addRow(QLabel('Раскодированный текст:'),
                           self.decoder_output)
        form_layout.addRow(QLabel('Длина раскодирования:'), self.length_input)
        form_layout.addRow(QLabel('Частоты символов:'),
                           self.frequencies_output)
        form_layout.addRow(QLabel('Вероятности:'),
                           self.probabilities_output)
        form_layout.addRow(QLabel('Процесс кодирования:'),
                           self.encode_process_output)
        form_layout.addRow(QLabel('Процесс декодирования:'),
                           self.decode_process_output)

        layout.addLayout(form_layout)

        encode_button = QPushButton('Кодировать')
        encode_button.clicked.connect(self.encode_text)
        decode_button = QPushButton('Декодировать')
        decode_button.clicked.connect(self.decode_text)

        layout.addWidget(encode_button)
        layout.addWidget(decode_button)

        self.setLayout(layout)

    def encode_text(self):
        text = self.input_text.toPlainText()
        frequencies = {char: text.count(char) for char in set(text)}
        probabilities = cumulative_probabilities(frequencies)
        code, encode_process = encode(text, probabilities)

        self.encoder_output.setPlainText(str(code))
        self.frequencies_output.setPlainText(str(frequencies))
        self.probabilities_output.setPlainText(str(probabilities))
        self.encode_process_output.setPlainText('\n'.join(encode_process))

    def decode_text(self):
        code_str = self.encoder_output.toPlainText()
        try:
            code = float(code_str)
            length = int(self.length_input.text())
            text = self.input_text.toPlainText()
            frequencies = {char: text.count(char) for char in set(text)}
            probabilities = cumulative_probabilities(frequencies)
            decoded_text, decode_process = decode(code, probabilities, length)

            self.decoder_output.setPlainText(decoded_text)
            self.decode_process_output.setPlainText('\n'.join(decode_process))
        except ValueError:
            self.decoder_output.setPlainText(
                'Ошибка: Введите корректный код и длину.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ArithmeticCodingApp()
    ex.show()
    sys.exit(app.exec_())
