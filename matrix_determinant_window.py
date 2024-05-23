from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QMessageBox, QGridLayout
import sys
import numpy as np


class DeterminantWindow(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.actual_size = 0
        self.stored_matrix = None
        self.matrix_widgets = []
        self.vbox = QtWidgets.QVBoxLayout()
        self.result_box = QVBoxLayout()

        self.initUI()

    def initUI(self):
        # Layout para el tamaño de la matriz
        size_layout = QHBoxLayout()
        self.size_label = QLabel("Ingrese el tamaño de la matriz:")
        self.size_input = QtWidgets.QLineEdit()
        self.size_input.setPlaceholderText("Tamaño de la matriz (N)")
        self.size_button = QtWidgets.QPushButton("Crear matriz")
        self.size_button.clicked.connect(self.create_matrix_input)

        size_layout.addWidget(self.size_label)
        size_layout.addWidget(self.size_input)
        size_layout.addWidget(self.size_button)
        self.vbox.addLayout(size_layout)

        # Espacio para los campos de entrada de la matriz
        self.matrix_layout = QGridLayout()
        self.matrix_widgets = []

        self.vbox.addLayout(self.matrix_layout)

        # Botón para obtener y mostrar la matriz
        self.get_matrix_button = QtWidgets.QPushButton("Guardar matriz")
        self.get_matrix_button.clicked.connect(self.get_matrix)
        self.get_matrix_button.setDisabled(True)

        self.determinant_button = QtWidgets.QPushButton("Calcular determinante")
        self.determinant_button.clicked.connect(self.calculate_determinant)
        self.determinant_button.setDisabled(True)

        self.vbox.addWidget(self.get_matrix_button)
        self.vbox.addWidget(self.determinant_button)

        self.vbox.addLayout(self.result_box)

        self.setLayout(self.vbox)
        self.setWindowTitle("Cálculo de Determinante de Matriz")
        self.show()

    def create_matrix_input(self):
        try:
            size = int(self.size_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error de entrada", "Por favor, ingrese un tamaño válido para la matriz.")
            return

        if size <= 0:
            QMessageBox.warning(self, "Error de entrada", "El tamaño de la matriz debe ser mayor que cero.")
            return

        self.actual_size = size

        # Limpia el layout anterior si existe
        for i in reversed(range(self.matrix_layout.count())):
            widget = self.matrix_layout.itemAt(i).widget()
            if widget is not None:
                self.matrix_layout.removeWidget(widget)
                widget.deleteLater()

        self.matrix_widgets = []

        # Crear campos de entrada para la matriz cuadrada de tamaño N
        for i in range(self.actual_size):
            row = []
            for j in range(self.actual_size):
                line_edit = QtWidgets.QLineEdit()
                self.matrix_layout.addWidget(line_edit, i, j)
                row.append(line_edit)
            self.matrix_widgets.append(row)
        self.get_matrix_button.setDisabled(False)
        self.determinant_button.setDisabled(True)

    def get_matrix(self):
        matrix = []

        # Recopilar valores de los campos de entrada
        try:
            for row_widgets in self.matrix_widgets:
                row = []
                for widget in row_widgets:
                    value = float(widget.text())
                    row.append(value)
                matrix.append(row)
        except ValueError:
            QMessageBox.warning(self, "Error de entrada", "Por favor, ingrese valores numéricos válidos en la matriz.")
            return

        self.stored_matrix = matrix
        print("Matriz ingresada:")
        print(self.stored_matrix)

        self.determinant_button.setDisabled(False)

    def calculate_determinant(self):
        matrix = self.stored_matrix
        size = len(matrix)
        if any(len(row) != size for row in matrix):
            QMessageBox.warning(self, "Error", "La matriz debe ser cuadrada.")
            return

        determinant, steps = self.laplace_determinant(matrix)
        self.display_result(matrix, determinant)

    def laplace_determinant(self, matrix):
        matrix = np.array(matrix)
        determinant = np.linalg.det(matrix)
        steps = [f"Determinante calculado usando numpy.linalg.det: {determinant:.2f}"]
        return determinant, steps

    def display_result(self, matrix, determinant):
        self.clear_layout(self.result_box)

        self.result_box.addWidget(QLabel("Matriz Original:"))
        self.result_box.addWidget(QLabel(self.format_matrix(matrix)))

        self.result_box.addWidget(QLabel(f"Determinante: {determinant:.2f}"))

    def format_matrix(self, matrix):
        formatted = ""
        for row in matrix:
            formatted += "| "
            for item in row:
                formatted += f"{item:.2f} "
            formatted += "|\n"
        return formatted.strip()

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def closeEvent(self, event):
        self.close_window()
        event.accept()

    def close_window(self):
        self.close()
        self.app.setVisible(True)
