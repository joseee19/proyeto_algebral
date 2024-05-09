from PyQt5 import QtWidgets
import numpy as np
from PyQt5.QtWidgets import QMessageBox


class InverseMatrixWindow(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.initUI()

    def initUI(self):
        # Layout general
        vbox = QtWidgets.QVBoxLayout()

        # Layout para el tamaño de la matriz
        size_layout = QtWidgets.QHBoxLayout()
        self.size_label = QtWidgets.QLabel("Ingrese el tamaño de la matriz:")
        self.size_input = QtWidgets.QLineEdit()
        self.size_input.setPlaceholderText("Tamaño de la matriz")
        self.size_button = QtWidgets.QPushButton("Crear matriz")
        self.size_button.clicked.connect(self.create_matrix_input)

        size_layout.addWidget(self.size_label)
        size_layout.addWidget(self.size_input)
        size_layout.addWidget(self.size_button)

        vbox.addLayout(size_layout)

        # Espacio para los campos de entrada de la matriz
        self.matrix_layout = QtWidgets.QGridLayout()
        self.matrix_widgets = []

        vbox.addLayout(self.matrix_layout)

        # Botón para obtener y mostrar la matriz
        self.get_matrix_button = QtWidgets.QPushButton("Obtener matriz inversa")
        self.get_matrix_button.clicked.connect(self.get_matrix)
        self.get_matrix_button.setDisabled(True)
        vbox.addWidget(self.get_matrix_button)

        self.setLayout(vbox)
        self.setWindowTitle("Matriz Cuadrada")
        self.show()

    def create_matrix_input(self):
        size = int(self.size_input.text())
        self.matrix_widgets = []

        # Limpia el layout anterior si existe
        for i in reversed(range(self.matrix_layout.count())):
            widget = self.matrix_layout.itemAt(i).widget()
            if widget is not None:
                self.matrix_layout.removeWidget(widget)
                widget.deleteLater()

        # Crear campos de entrada para la matriz cuadrada
        for i in range(size):
            row = []
            for j in range(size):
                line_edit = QtWidgets.QLineEdit()
                self.matrix_layout.addWidget(line_edit, i, j)
                row.append(line_edit)
            self.matrix_widgets.append(row)

        self.get_matrix_button.setDisabled(False)

    def get_matrix(self):
        size = len(self.matrix_widgets)
        matrix = []

        # Recopilar valores de los campos de entrada
        for row_widgets in self.matrix_widgets:
            row = []
            for widget in row_widgets:
                value = int(widget.text())
                row.append(value)
            matrix.append(row)

        print("Matriz ingresada:")
        for row in matrix:
            print(row)



        # Aquí puedes almacenar la matriz en una variable o usarla para otros fines
        self.stored_matrix = matrix
        self.get_inverse_matrix()

    def get_inverse_matrix(self):
        # Ejemplo de matriz cuadrada
        matrix = np.array(
            self.stored_matrix
        )
        # Asegúrate de que la matriz es cuadrada
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("La matriz debe ser cuadrada para obtener la inversa.")

        # Calcula el determinante para verificar si la matriz es invertible
        determinant = np.linalg.det(matrix)

        if determinant == 0:
            QMessageBox.critical(self, "Error", "La determinante de la matriz es 0")
        else:
            # Calcula la matriz inversa
            inverse_matrix = np.linalg.inv(matrix)

            QMessageBox.information(self, "Matriz inversa", f"El resultado de la matriz inversa es:\n{str(inverse_matrix)}")


    def closeEvent(self, event):
        self.close_window()
        event.accept()

    def close_window(self):
        self.close()
        self.app.setVisible(True)
