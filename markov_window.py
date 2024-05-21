from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QMessageBox
import numpy as np


class MarkovWindow(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.actual_row_size = 0
        self.actual_col_size = 0
        self.stored_matrix = None
        self.stored_matrix_initial = None
        self.matrix_widgets = []
        self.vbox = QVBoxLayout()
        self.result_box = QHBoxLayout()

        self.initUI()

    def initUI(self):
        # Layout para el tamaño de la matriz
        size_layout = QHBoxLayout()
        self.row_size_label = QLabel("Ingrese las filas de la matriz:")
        self.col_size_label = QLabel("Ingrese las columnas de la matriz:")
        self.row_input = QtWidgets.QLineEdit()
        self.col_input = QtWidgets.QLineEdit()

        self.cicles_label = QLabel("Ciclos:")
        self.cicles_input = QtWidgets.QLineEdit()

        self.row_input.setPlaceholderText("Filas de la matriz")
        self.col_input.setPlaceholderText("Columnas de la matriz")

        self.size_button = QtWidgets.QPushButton("Crear matriz")
        self.size_button.clicked.connect(self.create_matrix_input)

        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()
        horizontal_layout3 = QHBoxLayout()

        horizontal_layout1.addWidget(self.row_size_label)
        horizontal_layout1.addWidget(self.row_input)

        horizontal_layout2.addWidget(self.col_size_label)
        horizontal_layout2.addWidget(self.col_input)

        horizontal_layout3.addWidget(self.cicles_label)
        horizontal_layout3.addWidget(self.cicles_input)

        size_layout.addLayout(horizontal_layout1)
        size_layout.addLayout(horizontal_layout2)
        size_layout.addLayout(horizontal_layout3)

        size_layout.addWidget(self.size_button)

        self.vbox.addLayout(size_layout)

        # Espacio para los campos de entrada de la matriz
        self.matrix_layout = QtWidgets.QGridLayout()
        self.vbox.addLayout(self.matrix_layout)

        # Botones para obtener y mostrar las matrices
        self.get_matrix_A_button = QtWidgets.QPushButton("Guardar matriz A")
        self.get_matrix_A_button.clicked.connect(self.get_matrix_A)
        self.get_matrix_A_button.setDisabled(True)

        self.get_matrix_B_button = QtWidgets.QPushButton("Guardar matriz B")
        self.get_matrix_B_button.clicked.connect(self.get_matrix_B)
        self.get_matrix_B_button.setDisabled(True)

        self.multiplication_button = QtWidgets.QPushButton("Realizar operación")
        self.multiplication_button.clicked.connect(self.markov)

        self.vbox.addLayout(self.result_box)

        self.vbox.addWidget(self.get_matrix_A_button)
        self.vbox.addWidget(self.get_matrix_B_button)
        self.vbox.addWidget(self.multiplication_button)

        self.setLayout(self.vbox)
        self.setWindowTitle("Markov")
        self.show()

    def create_matrix_input(self):
        try:
            row_size = int(self.row_input.text())
            col_size = int(self.col_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error de entrada", "Por favor, ingrese valores enteros para filas y columnas.")
            return

        self.actual_row_size = row_size
        self.actual_col_size = col_size

        # Clear the previous layout if it exists
        for i in reversed(range(self.matrix_layout.count())):
            widget = self.matrix_layout.itemAt(i).widget()
            if widget is not None:
                self.matrix_layout.removeWidget(widget)
                widget.deleteLater()

        # Initialize matrix_widgets list
        self.matrix_widgets = []

        # Create input fields for the matrix
        for i in range(row_size):
            row = []
            for j in range(col_size):
                line_edit = QtWidgets.QLineEdit()
                self.matrix_layout.addWidget(line_edit, i, j)
                row.append(line_edit)
            self.matrix_widgets.append(row)

        # Enable buttons to get matrices
        self.get_matrix_A_button.setDisabled(False)
        self.get_matrix_B_button.setDisabled(False)

    def get_matrix(self, is_matrix_A):
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

        # Almacenar la matriz
        if is_matrix_A:
            self.stored_matrix = matrix
            print("Matriz A ingresada:")
        else:
            self.stored_matrix_initial = matrix
            print("Matriz B ingresada:")

        for row in matrix:
            print(row)

    def get_matrix_A(self):
        self.get_matrix(True)

    def get_matrix_B(self):
        self.get_matrix(False)

    def multiplicacion(self, matrix1, matrix2):
        if len(matrix1[0]) != len(matrix2):
            raise ValueError('No es posible la multiplicación')

        result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix1[0])):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        return result

    def markov(self):
        if self.stored_matrix is None or self.stored_matrix_initial is None:
            QMessageBox.warning(self, "Error", "Por favor, asegúrese de ingresar ambas matrices antes de realizar la operación.")
            return

        try:
            cicles = int(self.cicles_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error de entrada", "Por favor, ingrese un número entero válido para los ciclos.")
            return

        matrix = np.transpose(self.stored_matrix)
        key = self.stored_matrix_initial

        print('Bienvenido al programa')

        try:
            for _ in range(cicles):
                key = self.multiplicacion(matrix, key)
        except ValueError as e:
            QMessageBox.warning(self, "Error de multiplicación", str(e))
            return

        print('El resultado de la matriz final es:')
        for row in key:
            print(row)

        value_a = self.format_matrix(matrix)
        value_b = self.format_matrix(self.stored_matrix_initial)
        value_result = self.format_matrix(key)
        self.display_result(value_a, value_b, value_result, cicles)

    def format_matrix(self, matrix):
        formatted = ""
        for row in matrix:
            formatted += "|"
            for item in row:
                formatted += f"{item} "
            formatted += "|\n"
        return formatted.strip()

    def display_result(self, value_a, value_b, value_result, cicles):
        self.clear_layout(self.result_box)

        self.result_box.addWidget(QLabel(f'Resultado luego de {cicles} ciclos es:'))
        self.result_box.addWidget(QLabel(f"{value_a}"))
        self.result_box.addWidget(QLabel('*'))
        self.result_box.addWidget(QLabel(f"{value_b}"))
        self.result_box.addWidget(QLabel('='))
        self.result_box.addWidget(QLabel(f"{value_result}"))

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
