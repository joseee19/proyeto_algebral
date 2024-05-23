from PyQt5 import QtWidgets
import numpy as np
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QGridLayout


class EncryptionWindow(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.initUI()

    def initUI(self):
        # Layout general
        self.vbox = QVBoxLayout()

        # Layout para el mensaje
        message_layout = QHBoxLayout()
        self.message_label = QLabel("Ingrese el mensaje:")
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Mensaje a cifrar o descifrar")
        message_layout.addWidget(self.message_label)
        message_layout.addWidget(self.message_input)
        self.vbox.addLayout(message_layout)

        # Layout para la matriz llave 3x3
        key_layout = QGridLayout()
        self.key_widgets = []
        key_layout.addWidget(QLabel("Ingrese la llave (matriz 3x3):"), 0, 0, 1, 3)
        for i in range(3):
            row = []
            for j in range(3):
                line_edit = QLineEdit()
                key_layout.addWidget(line_edit, i + 1, j)
                row.append(line_edit)
            self.key_widgets.append(row)
        self.vbox.addLayout(key_layout)

        # Layout para mostrar el mensaje cifrado o descifrado
        self.layout_mensaje = QHBoxLayout()
        self.vbox.addLayout(self.layout_mensaje)

        # Botón para cifrar el mensaje
        self.encrypt_button = QPushButton("Cifrar mensaje")
        self.encrypt_button.clicked.connect(self.encrypt_message)
        self.vbox.addWidget(self.encrypt_button)

        # Botón para descifrar el mensaje
        self.decrypt_button = QPushButton("Descifrar mensaje")
        self.decrypt_button.clicked.connect(self.decrypt_message)
        self.vbox.addWidget(self.decrypt_button)

        self.setLayout(self.vbox)
        self.setWindowTitle("Cifrado y Descifrado de Mensaje con Matriz Llave 3x3")
        self.show()

    def get_key_matrix(self):
        matrix = []
        try:
            for row_widgets in self.key_widgets:
                row = []
                for widget in row_widgets:
                    value = int(widget.text())
                    row.append(value)
                matrix.append(row)
            return np.array(matrix)
        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, ingrese solo números enteros en la matriz.")
            return None

    def encrypt_message(self):
        key_matrix = self.get_key_matrix()
        if key_matrix is None:
            return

        message = self.message_input.text().upper().replace(" ", "")
        if len(message) % 3 != 0:
            message += 'X' * (3 - len(message) % 3)  # Rellenar con 'X' para que el mensaje tenga longitud múltiplo de 3

        message_matrix = []
        for i in range(0, len(message), 3):
            chunk = [ord(char) - 65 for char in message[i:i + 3]]
            message_matrix.append(chunk)

        encrypted_matrix = []
        for vector in message_matrix:
            encrypted_vector = np.dot(key_matrix, vector) % 26
            encrypted_matrix.append(encrypted_vector)

        encrypted_message = ''.join([''.join([chr(num + 65) for num in vector]) for vector in encrypted_matrix])
        self.clear_layout()
        self.layout_mensaje.addWidget(QLabel(f"Mensaje cifrado:\n{encrypted_message}"))

    def decrypt_message(self):
        key_matrix = self.get_key_matrix()
        if key_matrix is None:
            return

        # Verificar si la matriz llave es invertible (determinante distinto de cero)
        determinant = int(round(np.linalg.det(key_matrix)))
        if determinant == 0:
            QMessageBox.critical(self, "Error", "La matriz llave no es invertible.")
            return

        try:
            # Calcular la matriz inversa en el campo mod 26
            determinant_inv = pow(determinant, -1, 26)  # Inverso modular del determinante
            adjugate = np.round(np.linalg.inv(key_matrix) * determinant).astype(int)
            inverse_key_matrix = (determinant_inv * adjugate) % 26
        except np.linalg.LinAlgError:
            QMessageBox.critical(self, "Error", "Ocurrió un error al calcular la matriz inversa.")
            return

        message = self.message_input.text().upper().replace(" ", "")

        if len(message) % 3 != 0:
            QMessageBox.critical(self, "Error", "La longitud del mensaje cifrado debe ser múltiplo de 3.")
            return

        if not message.isalpha():  # Verificar si el mensaje cifrado contiene solo letras del alfabeto
            QMessageBox.critical(self, "Error", "El mensaje cifrado debe contener solo letras del alfabeto.")
            return

        message_matrix = []
        for i in range(0, len(message), 3):
            chunk = [ord(char) - 65 for char in message[i:i + 3]]
            message_matrix.append(chunk)

        decrypted_matrix = []
        for vector in message_matrix:
            decrypted_vector = np.dot(inverse_key_matrix, vector) % 26
            decrypted_matrix.append(decrypted_vector)

        decrypted_message = ''.join([''.join([chr(num + 65) for num in vector]) for vector in decrypted_matrix])
        self.clear_layout()
        self.layout_mensaje.addWidget(QLabel(f"Mensaje descifrado:\n{decrypted_message}"))

    def clear_layout(self):
        while self.layout_mensaje.count():
            item = self.layout_mensaje.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def closeEvent(self, event):
        self.close_window()
        event.accept()

    def close_window(self):
        self.close()
        self.app.setVisible(True)
