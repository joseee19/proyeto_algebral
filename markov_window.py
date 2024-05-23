from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QMessageBox, QSpacerItem, QSizePolicy
import numpy as np


class MarkovWindow(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.stored_matrix = None
        self.stored_matrix_initial = None
        self.matrix_widgets1 = []
        self.matrix_widgets2 = []
        self.vbox = QVBoxLayout()
        self.result_box = QHBoxLayout()

        self.initUI()

    def initUI(self):
        # Layout para el tamaño de la matriz
        size_layout = QHBoxLayout()
        self.cicles_label = QLabel("Ciclos:")
        self.cicles_input = QtWidgets.QLineEdit()
        self.cicles_input.setFixedSize(35, 23)

        horizontal_layout1 = QHBoxLayout()
        horizontal_layout3 = QHBoxLayout()

        horizontal_layout3.addWidget(self.cicles_label)
        horizontal_layout3.addWidget(self.cicles_input)
        horizontal_layout3.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))


        size_layout.addLayout(horizontal_layout1)
        size_layout.addLayout(horizontal_layout3)


        # Espacio para los campos de entrada de la matriz
        self.matrix_layout1 = QtWidgets.QGridLayout()
        self.matrix_layout2 = QtWidgets.QGridLayout()
        self.vbox.addWidget(QLabel("Ingrese la matriz de transición: "))
        self.vbox.addLayout(self.matrix_layout1)
        self.vbox.addWidget(QLabel("Ingrese la matriz de probabilidades iniciales: "))
        self.vbox.addLayout(self.matrix_layout2)
        self.vbox.addLayout(size_layout)



        # Botones para obtener y mostrar las matrices
        self.get_matrix_A_button = QtWidgets.QPushButton("Guardar matriz A")
        self.get_matrix_A_button.clicked.connect(self.get_matrix_A)
        self.get_matrix_A_button.setDisabled(False)

        self.get_matrix_B_button = QtWidgets.QPushButton("Guardar matriz B")
        self.get_matrix_B_button.clicked.connect(self.get_matrix_B)
        self.get_matrix_B_button.setDisabled(False)

        self.multiplication_button = QtWidgets.QPushButton("Realizar operación")
        self.multiplication_button.clicked.connect(self.markov)

        self.vbox.addLayout(self.result_box)

        self.vbox.addWidget(self.multiplication_button)
        self.create_matrix_input(3, 3)
        self.create_matrix_input1(3, 1)

        self.setLayout(self.vbox)
        self.setWindowTitle("Markov")
        self.show()

    def create_matrix_input(self, row, col):
        row_size = row
        col_size = col

        self.matrix_widgets1 = []

        for i in range(row_size):
            row = []
            for j in range(col_size):
                line_edit = QtWidgets.QLineEdit()
                self.matrix_layout1.addWidget(line_edit, i, j)
                row.append(line_edit)
            self.matrix_widgets1.append(row)

    def create_matrix_input1(self, row, col):
        row_size = row
        col_size = col

        self.matrix_widgets2 = []

        for i in range(row_size):
            row = []
            for j in range(col_size):
                line_edit = QtWidgets.QLineEdit()
                line_edit.setFixedSize(35, 20)
                self.matrix_layout2.addWidget(line_edit, i, j)
                row.append(line_edit)
            self.matrix_widgets2.append(row)

    def get_matrix(self, is_matrix_A):
        matrix = []

        try:
            widgets_list = self.matrix_widgets1 if is_matrix_A else self.matrix_widgets2
            for row_widgets in widgets_list:
                row = []
                for widget in row_widgets:
                    value = float(widget.text())
                    row.append(value)
                matrix.append(row)
        except ValueError:
            QMessageBox.warning(self, "Error de entrada", "Por favor, ingrese valores numéricos válidos en la matriz.")
            return

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
        self.get_matrix(True)
        self.get_matrix(False)
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
