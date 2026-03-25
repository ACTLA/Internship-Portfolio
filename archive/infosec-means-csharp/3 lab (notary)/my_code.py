import os
import shutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout, QMessageBox
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

BASE_DIR = r"C:\PythonProjects\SoftwareAndHardwareMeansOfInformationProtection\3 lab (notary)\simulation"
SENDER_DIR = os.path.join(BASE_DIR, "sender")
NOTARY_DIR = os.path.join(BASE_DIR, "notary")
RECIPIENT_DIR = os.path.join(BASE_DIR, "recipient")


def setup_directories():
    os.makedirs(SENDER_DIR, exist_ok=True)
    os.makedirs(NOTARY_DIR, exist_ok=True)
    os.makedirs(RECIPIENT_DIR, exist_ok=True)


setup_directories()


class SenderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Отправитель")
        self.setGeometry(100, 100, 400, 250)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.label = QLabel("Выберите файлы для отправки нотариусу:", self)
        self.layout.addWidget(self.label)

        self.send_to_notary_button = QPushButton(
            "Выбрать файлы и отправить нотариусу", self)
        self.send_to_notary_button.clicked.connect(
            self.browse_and_send_files_to_notary)
        self.layout.addWidget(self.send_to_notary_button)

        self.send_to_recipient_button = QPushButton(
            "Выбрать файлы и отправить получателю", self)
        self.send_to_recipient_button.clicked.connect(
            self.browse_and_send_files_to_recipient)
        self.layout.addWidget(self.send_to_recipient_button)

        self.setLayout(self.layout)

    def browse_and_send_files_to_notary(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, "Выберите файлы для отправки нотариусу")
        if not file_paths:
            return

        for file_path in file_paths:
            shutil.copy(file_path, NOTARY_DIR)

        QMessageBox.information(self, "Успех", "Файлы отправлены нотариусу.")

    def browse_and_send_files_to_recipient(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, "Выберите файлы для отправки получателю")
        if not file_paths:
            return

        for file_path in file_paths:
            shutil.copy(file_path, RECIPIENT_DIR)

        QMessageBox.information(self, "Успех", "Файлы отправлены получателю.")


class NotaryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Нотариус")
        self.setGeometry(100, 100, 400, 250)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.generate_keys_button = QPushButton("Сгенерировать ключи", self)
        self.generate_keys_button.clicked.connect(self.generate_keys)
        self.layout.addWidget(self.generate_keys_button)

        self.select_and_sign_button = QPushButton(
            "Выбрать и подписать файл", self)
        self.select_and_sign_button.clicked.connect(self.select_and_sign_file)
        self.layout.addWidget(self.select_and_sign_button)

        self.send_files_button = QPushButton(
            "Выбрать файлы и отправить отправителю", self)
        self.send_files_button.clicked.connect(
            self.browse_and_send_files_to_sender)
        self.layout.addWidget(self.send_files_button)

        self.send_public_key_button = QPushButton(
            "Отправить публичный ключ получателю", self)
        self.send_public_key_button.clicked.connect(
            self.send_public_key_to_recipient)
        self.layout.addWidget(self.send_public_key_button)

        self.setLayout(self.layout)

        self.selected_file = None

    def generate_keys(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        with open(os.path.join(NOTARY_DIR, "private_key.pem"), "wb") as priv_file:
            priv_file.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))

        with open(os.path.join(NOTARY_DIR, "public_key.pem"), "wb") as pub_file:
            pub_file.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

        QMessageBox.information(self, "Успех", "Ключи сгенерированы.")

    def select_and_sign_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл для подписи")
        if file_path:
            self.selected_file = file_path

            private_key_path = os.path.join(NOTARY_DIR, "private_key.pem")
            if not os.path.exists(private_key_path):
                QMessageBox.critical(
                    self, "Ошибка", "Приватный ключ не найден.")
                return

            with open(private_key_path, "rb") as priv_file:
                private_key = serialization.load_pem_private_key(
                    priv_file.read(), password=None)

            with open(self.selected_file, "rb") as f:
                file_data = f.read()

            signature = private_key.sign(
                file_data, PKCS1v15(), hashes.SHA256())

            signature_file_path = self.selected_file + ".sig"
            with open(signature_file_path, "wb") as sig_file:
                sig_file.write(signature)

            shutil.copy(self.selected_file, SENDER_DIR)
            shutil.copy(signature_file_path, SENDER_DIR)

            QMessageBox.information(self, "Успех", "Файл подписан.")

    def browse_and_send_files_to_sender(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self, "Выберите файлы для отправки отправителю")
        if not file_paths:
            return

        for file_path in file_paths:
            shutil.copy(file_path, SENDER_DIR)

        QMessageBox.information(self, "Успех", "Файлы отправлены отправителю.")

    def send_public_key_to_recipient(self):
        public_key_path = os.path.join(NOTARY_DIR, "public_key.pem")
        if not os.path.exists(public_key_path):
            QMessageBox.critical(self, "Ошибка", "Публичный ключ не найден.")
            return

        shutil.copy(public_key_path, RECIPIENT_DIR)
        QMessageBox.information(
            self, "Успех", "Публичный ключ отправлен получателю.")


class RecipientApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Получатель")
        self.setGeometry(100, 100, 400, 200)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.verify_button = QPushButton("Проверить подпись", self)
        self.verify_button.clicked.connect(self.verify_signature)
        self.layout.addWidget(self.verify_button)

        self.setLayout(self.layout)

    def verify_signature(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл для проверки", RECIPIENT_DIR)
        if not file_path:
            return

        sig_path, _ = QFileDialog.getOpenFileName(
            self, "Выберите подпись для проверки", RECIPIENT_DIR, "Файлы подписи (*.sig)")
        if not sig_path:
            return

        public_key_path = os.path.join(RECIPIENT_DIR, "public_key.pem")
        if not os.path.exists(public_key_path):
            QMessageBox.critical(self, "Ошибка", "Публичный ключ не найден.")
            return

        with open(public_key_path, "rb") as pub_file:
            public_key = serialization.load_pem_public_key(pub_file.read())

        with open(file_path, "rb") as f:
            file_data = f.read()
        with open(sig_path, "rb") as s:
            signature = s.read()

        try:
            public_key.verify(signature, file_data,
                              PKCS1v15(), hashes.SHA256())
            QMessageBox.information(self, "Успех", "Подпись подтверждена.")
        except Exception:
            QMessageBox.critical(self, "Ошибка", "Подпись не подтверждена.")


if __name__ == "__main__":
    app = QApplication([])

    sender_app = SenderApp()
    sender_app.show()

    notary_app = NotaryApp()
    notary_app.show()

    recipient_app = RecipientApp()
    recipient_app.show()

    app.exec()
