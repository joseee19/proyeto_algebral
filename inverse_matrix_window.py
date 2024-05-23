from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QMessageBox, QGridLayout
import numpy as np


class InverseMatrixWindow(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.actual_row_size = 0
        self.actual_col_size = 0
        self.stored_matrix = None
        self.matrix_widgets = []
        self.vbox = QtWidgets.QVBoxLayout()
        self.result_box = QVBoxLayout()

        self.initUI()

    def initUI(self):
        # Layout para el tamaño de la matriz
        size_layout = QHBoxLayout()
        self.row_size = QtWidgets.QLabel("Ingrese el tamaño de la matriz:")
        self.row_input = QtWidgets.QLineEdit()

        self.row_input.setPlaceholderText("Tamaño de la matriz")

        self.size_button = QtWidgets.QPushButton("Crear matriz")
        self.size_button.clicked.connect(self.create_matrix_input)

        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()

        horizontal_layout1.addWidget(self.row_size)
        horizontal_layout1.addWidget(self.row_input)

        size_layout.addLayout(horizontal_layout1)
        size_layout.addLayout(horizontal_layout2)

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

        self.inverse_button = QtWidgets.QPushButton("Calcular inversa")
        self.inverse_button.clicked.connect(self.calculate_inverse)
        self.inverse_button.setDisabled(True)

        self.vbox.addWidget(self.get_matrix_button)
        self.vbox.addWidget(self.inverse_button)

        self.vbox.addLayout(self.result_box)

        self.setLayout(self.vbox)
        self.setWindowTitle("Cálculo de Matriz Inversa")
        self.show()

    def create_matrix_input(self):
        try:
            row_size = int(self.row_input.text())
            col_size = int(self.row_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error de entrada",
                                "Por favor, ingrese valores numéricos válidos para filas y columnas.")
            return

        if row_size != col_size:
            QMessageBox.warning(self, "Error de entrada",
                                "Por favor, ingrese una matriz cuadrada (mismo número de filas y columnas).")
            return

        self.actual_row_size = row_size
        self.actual_col_size = row_size

        # Limpia el layout anterior si existe
        for i in reversed(range(self.matrix_layout.count())):
            widget = self.matrix_layout.itemAt(i).widget()
            if widget is not None:
                self.matrix_layout.removeWidget(widget)
                widget.deleteLater()

        self.matrix_widgets = []

        # Crear campos de entrada para la matriz cuadrada
        for i in range(row_size):
            row = []
            for j in range(col_size):
                line_edit = QtWidgets.QLineEdit()
                self.matrix_layout.addWidget(line_edit, i, j)
                row.append(line_edit)
            self.matrix_widgets.append(row)
        self.get_matrix_button.setDisabled(False)
        self.inverse_button.setDisabled(True)

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

        self.stored_matrix = np.array(matrix)
        print("Matriz ingresada:")
        print(self.stored_matrix)

        self.inverse_button.setDisabled(False)

    def calculate_inverse(self):
        self.get_matrix()
        try:
            matrix = self.stored_matrix
            inverse_matrix = np.linalg.inv(matrix)
        except np.linalg.LinAlgError:
            QMessageBox.warning(self, "Error", "La matriz no es invertible.")
            return

        steps = self.gaussian_elimination_steps(matrix)

        self.display_result(matrix, inverse_matrix, steps)

    def gaussian_elimination_steps(self, matrix):
        n = len(matrix)
        a = np.hstack((matrix, np.eye(n)))
        steps = []

        for i in range(n):
            max_row = max(range(i, n), key=lambda r: abs(a[r][i]))
            if i != max_row:
                a[[i, max_row]] = a[[max_row, i]]
                steps.append(a.copy())

            for j in range(i + 1, n):
                factor = a[j][i] / a[i][i]
                a[j] = a[j] - factor * a[i]
                steps.append(a.copy())

        for i in range(n - 1, -1, -1):
            a[i] = a[i] / a[i][i]
            steps.append(a.copy())

            for j in range(i):
                factor = a[j][i]
                a[j] = a[j] - factor * a[i]
                steps.append(a.copy())

        return steps

    def display_result(self, matrix, inverse_matrix, steps):
        self.clear_layout(self.result_box)

        self.result_box.addWidget(QLabel("Matriz Original:"))
        self.result_box.addWidget(QLabel(self.format_matrix(matrix)))

        self.result_box.addWidget(QLabel("Pasos de eliminación gaussiana:"))
        for step in steps:
            self.result_box.addWidget(QLabel(self.format_matrix(step)))

        self.result_box.addWidget(QLabel("Matriz Inversa:"))
        self.result_box.addWidget(QLabel(self.format_matrix(inverse_matrix)))

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

