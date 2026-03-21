import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTextEdit, QFileDialog, QFrame, QTabWidget, QTextBrowser
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from pathlib import Path
import random
from hashlib import sha256
from typing import Tuple, Optional, Union


class GOSTSignature:
    def __init__(self, p: int, q: int, alpha: int):
        self.p = p
        self.q = q
        self.alpha = alpha

        if not self._validate_parameters():
            raise ValueError("Некорректные параметры")

    def _validate_parameters(self) -> bool:
        if not (1 < self.alpha < self.p):
            return False
        if pow(self.alpha, self.q, self.p) != 1:
            return False
        return True

    def _hash_data(self, data: Union[str, bytes]) -> int:
        """Хеширование данных с усилением крипто-стойкости"""
        if isinstance(data, str):
            data = data.encode()

        # Используем двойное хеширование для усиления крипто-стойкости
        hash1 = sha256(data).digest()
        hash2 = sha256(hash1).digest()
        hash_value = int.from_bytes(hash2, 'big')

        # Приводим хеш к диапазону [1, q-1]
        hash_value = (hash_value % (self.q - 1)) + 1

        print(f"Debug: Hash value = {hash_value}")
        return hash_value

    def generate_keypair(self) -> Tuple[int, int]:
        """Генерация пары ключей"""
        # Генерируем закрытый ключ в диапазоне [2, q-1]
        private_key = random.randrange(2, self.q)
        # Вычисляем открытый ключ
        public_key = pow(self.alpha, private_key, self.p)
        return private_key, public_key

    def sign_file(self, file_path: Union[str, Path], private_key: int) -> Optional[Tuple[int, int]]:
        """Подписать файл"""
        print(f"\nПодписываем файл: {file_path}")
        file_path = Path(file_path)
        with open(file_path, 'rb') as f:
            file_data = f.read()
        H = self._hash_data(file_data)
        return self._create_signature(H, private_key)

    def _create_signature(self, H: int, private_key: int) -> Optional[Tuple[int, int]]:
        """Создание подписи"""
        while True:
            # Генерируем случайное k в диапазоне [1, q-1]
            k = random.randrange(1, self.q)

            # Вычисляем первую часть подписи
            R = pow(self.alpha, k, self.p) % self.q

            if R == 0:
                continue

            # Вычисляем вторую часть подписи
            S = (k * H + private_key * R) % self.q

            if S != 0:
                print(f"Debug: Generated signature - R={R}, S={S}")
                return R, S

    def verify_file(self, file_path: Union[str, Path], signature: Tuple[int, int], public_key: int) -> bool:
        """Проверить подпись файла"""
        print(f"\nПроверяем файл: {file_path}")
        file_path = Path(file_path)
        with open(file_path, 'rb') as f:
            file_data = f.read()
        H = self._hash_data(file_data)
        return self._verify_signature(H, signature, public_key)

    def _verify_signature(self, H: int, signature: Tuple[int, int], public_key: int) -> bool:
        """Проверка подписи"""
        R, S = signature
        print(f"Debug: Verifying signature - R={R}, S={S}")

        # Проверка диапазонов
        if not (0 < R < self.q and 0 < S < self.q):
            print("Debug: Signature values out of range")
            return False

        # Проверка подписи по формуле ГОСТ Р 34.10-94
        try:
            # Вычисляем v = H^(-1) mod q
            v = pow(H, -1, self.q)
            print(f"Debug: v = {v}")

            # Вычисляем z1 = (S * v) mod q
            z1 = (S * v) % self.q
            print(f"Debug: z1 = {z1}")

            # Вычисляем z2 = (-R * v) mod q
            z2 = (-R * v) % self.q
            print(f"Debug: z2 = {z2}")

            # Вычисляем результат
            result = (pow(self.alpha, z1, self.p) *
                      pow(public_key, z2, self.p)) % self.p % self.q
            print(f"Debug: Final verification result = {result}")
            print(f"Debug: Should match R = {R}")

            return result == R

        except Exception as e:
            print(f"Debug: Verification error - {e}")
            return False


def generate_prime(bits):
    while True:
        n = random.getrandbits(bits)
        n |= (1 << bits - 1) | 1
        if is_prime(n):
            return n


def is_prime(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    def miller_rabin_test(d, n):
        a = 2 + random.randint(1, n - 4)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for i in range(k):
        if not miller_rabin_test(d, n):
            return False
    return True


def generate_parameters(p_bits=16, q_bits=8):
    while True:
        q = generate_prime(q_bits)
        k = 2
        while k < (1 << (p_bits - q_bits)):
            p = k * q + 1
            if p.bit_length() <= p_bits and is_prime(p):
                for alpha in range(2, p):
                    if pow(alpha, q, p) == 1:
                        return p, q, alpha
            k += 1


class GOSTSignatureGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ГОСТ Р 34.10-94 Цифровая подпись")
        self.setGeometry(100, 100, 1400, 900)
        self.initialize_gost()
        self._create_widgets()

    def initialize_gost(self):
        self.p, self.q, self.alpha = generate_parameters()
        self.gost = GOSTSignature(self.p, self.q, self.alpha)
        self.private_key, self.public_key = self.gost.generate_keypair()

    def _create_widgets(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        self._create_info_frame(main_widget)
        content_frame = QFrame()
        content_layout = QHBoxLayout(content_frame)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(10)

        sign_frame = QFrame()
        sign_frame.setFrameShape(QFrame.StyledPanel)
        sign_frame.setFrameShadow(QFrame.Raised)
        sign_layout = QVBoxLayout(sign_frame)
        sign_layout.setContentsMargins(10, 10, 10, 10)

        verify_frame = QFrame()
        verify_frame.setFrameShape(QFrame.StyledPanel)
        verify_frame.setFrameShadow(QFrame.Raised)
        verify_layout = QVBoxLayout(verify_frame)
        verify_layout.setContentsMargins(10, 10, 10, 10)

        content_layout.addWidget(sign_frame, 1)
        content_layout.addWidget(verify_frame, 1)

        main_layout.addWidget(content_frame)

        self._create_sign_widgets(sign_frame)
        self._create_verify_widgets(verify_frame)

    def _create_info_frame(self, parent):
        info_frame = QFrame(parent)
        info_frame.setFrameShape(QFrame.StyledPanel)
        info_frame.setFrameShadow(QFrame.Raised)
        info_layout = QVBoxLayout(info_frame)
        info_layout.setContentsMargins(10, 10, 10, 10)

        calc_frame = QFrame()
        calc_frame.setFrameShape(QFrame.StyledPanel)
        calc_frame.setFrameShadow(QFrame.Raised)
        calc_layout = QVBoxLayout(calc_frame)
        calc_layout.setContentsMargins(10, 10, 10, 10)

        calc_text = (
            "1) Необходимо сгенерировать случайное k, 1 < k < q;\n"
            "2) R = (alpha^k mod p) mod q — первая часть подписи;\n"
            "3) H = Hash(m), где Hash — хеш-функция, m — подписываемое сообщение;\n"
            "4) S = kH + zR mod q, где z — закрытый ключ;\n"
            "5) Если S=0, то повторить операции 1-4."
        )

        calc_label = QLabel(calc_text, calc_frame)
        calc_label.setFont(QFont('Helvetica', 12))
        calc_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        calc_label.setWordWrap(True)
        calc_layout.addWidget(calc_label)

        verify_frame = QFrame()
        verify_frame.setFrameShape(QFrame.StyledPanel)
        verify_frame.setFrameShadow(QFrame.Raised)
        verify_layout = QVBoxLayout(verify_frame)
        verify_layout.setContentsMargins(10, 10, 10, 10)

        verify_text = (
            "1) 0 < R < q или 0 < S < q. Если хотя бы одно из двух условий не\n"
            "   выполнено, то подпись недействительна. Иначе:\n"
            "2) R' = (alpha^{R/h} y^{S/H} mod p) mod q, где y — открытый ключ;\n"
            "3) Если R = R', то подпись действительна."
        )

        verify_label = QLabel(verify_text, verify_frame)
        verify_label.setFont(QFont('Helvetica', 12))
        verify_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        verify_label.setWordWrap(True)
        verify_layout.addWidget(verify_label)

        info_layout.addWidget(calc_frame, 1)
        info_layout.addWidget(verify_frame, 1)

    def _create_sign_widgets(self, parent):
        # Параметры системы и ключи в одном окне
        system_info_label = QLabel("Параметры системы и ключи:", parent)
        system_info_label.setFont(QFont('Helvetica', 12, QFont.Bold))
        system_info_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        system_info = QTextBrowser(parent)
        system_info.setReadOnly(True)
        system_info.setPlainText(
            f"Параметры системы:\n"
            f"p = {self.p}\n"
            f"q = {self.q}\n"
            f"alpha = {self.alpha}\n\n"
            f"Ключи:\n"
            f"Закрытый ключ: {self.private_key}\n"
            f"Открытый ключ: {self.public_key}\n"
        )

        # Выбор файла
        self.file_var = ""
        file_frame = QFrame(parent)
        file_layout = QHBoxLayout(file_frame)

        file_label = QLabel("Выберите файл:", file_frame)
        file_label.setFont(QFont('Helvetica', 12, QFont.Bold))

        self.file_entry = QTextEdit(file_frame)
        self.file_entry.setReadOnly(True)
        self.file_entry.setMaximumHeight(30)

        browse_button = QPushButton("Обзор", file_frame)
        browse_button.clicked.connect(self._browse_file)

        file_layout.addWidget(file_label)
        file_layout.addWidget(self.file_entry, 1)
        file_layout.addWidget(browse_button)

        # Кнопка подписи
        sign_button = QPushButton("Подписать", parent)
        sign_button.clicked.connect(self._sign)

        # Результат подписи
        result_label = QLabel("Подпись:", parent)
        result_label.setFont(QFont('Helvetica', 12, QFont.Bold))

        self.signature_output = QTextEdit(parent)
        self.signature_output.setReadOnly(True)

        parent.layout().addWidget(system_info_label)
        parent.layout().addWidget(system_info)
        parent.layout().addWidget(file_frame)
        parent.layout().addWidget(sign_button)
        parent.layout().addWidget(result_label)
        parent.layout().addWidget(self.signature_output)

    def _create_verify_widgets(self, parent):
        # Ввод подписи
        verify_signature_label = QLabel("Введите подпись (R,S):", parent)
        verify_signature_label.setFont(QFont('Helvetica', 12, QFont.Bold))

        self.verify_signature = QTextEdit(parent)

        # Выбор файла
        self.verify_file_var = ""
        file_frame = QFrame(parent)
        file_layout = QHBoxLayout(file_frame)

        file_label = QLabel("Выберите файл:", file_frame)
        file_label.setFont(QFont('Helvetica', 12, QFont.Bold))

        self.verify_file_entry = QTextEdit(file_frame)
        self.verify_file_entry.setReadOnly(True)
        self.verify_file_entry.setMaximumHeight(30)

        browse_button = QPushButton("Обзор", file_frame)
        browse_button.clicked.connect(self._browse_verify_file)

        file_layout.addWidget(file_label)
        file_layout.addWidget(self.verify_file_entry, 1)
        file_layout.addWidget(browse_button)

        # Кнопка проверки
        verify_button = QPushButton("Проверить", parent)
        verify_button.clicked.connect(self._verify)

        # Результат проверки
        result_label = QLabel("Результат проверки:", parent)
        result_label.setFont(QFont('Helvetica', 12, QFont.Bold))

        self.verify_result = QTextEdit(parent)
        self.verify_result.setReadOnly(True)

        parent.layout().addWidget(verify_signature_label)
        parent.layout().addWidget(self.verify_signature)
        parent.layout().addWidget(file_frame)
        parent.layout().addWidget(verify_button)
        parent.layout().addWidget(result_label)
        parent.layout().addWidget(self.verify_result)

    def _browse_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл", "", "All Files (*);;Text Files (*.txt)")
        if filename:
            self.file_entry.setPlainText(filename)
            self.file_var = filename

    def _browse_verify_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл", "", "All Files (*);;Text Files (*.txt)")
        if filename:
            self.verify_file_entry.setPlainText(filename)
            self.verify_file_var = filename

    def _sign(self):
        try:
            if not self.file_var:
                raise ValueError("Выберите файл для подписи")

            signature = self.gost.sign_file(self.file_var, self.private_key)
            self.signature_output.setPlainText(
                f"R = {signature[0]}\n"
                f"S = {signature[1]}"
            )

        except Exception as e:
            self.signature_output.setPlainText(f"Ошибка: {str(e)}")

    def _verify(self):
        try:
            if not self.verify_file_var:
                raise ValueError("Выберите файл для проверки")

            # Получаем подпись
            sig_text = self.verify_signature.toPlainText()
            r_line, s_line = sig_text.strip().split('\n')
            r = int(r_line.split('=')[1].strip())
            s = int(s_line.split('=')[1].strip())
            signature = (r, s)

            # Проверяем подпись
            is_valid = self.gost.verify_file(
                self.verify_file_var, signature, self.public_key)
            self.verify_result.setPlainText(
                "Подпись верна!" if is_valid else "Подпись неверна!")

        except Exception as e:
            self.verify_result.setPlainText(f"Ошибка: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GOSTSignatureGUI()
    window.show()
    sys.exit(app.exec_())
