from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout


class SumSubMatrixWindow(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.actual_row_size = 0
        self.actual_col_size = 0
        self.stored_matrix_A = None
        self.stored_matrix_B = None
        self.matrix_widgets = []
        self.vbox = QtWidgets.QVBoxLayout()
        self.result_box = QHBoxLayout()

        self.initUI()

    def initUI(self):
        # Layout general

        # Layout para el tamaño de la matriz
        size_layout = QHBoxLayout()
        self.row_size = QtWidgets.QLabel("Ingrese las filas de la matriz:")
        self.col_size = QtWidgets.QLabel("Ingrese las columnas de la matriz:")
        self.row_input = QtWidgets.QLineEdit()
        self.col_input = QtWidgets.QLineEdit()

        self.row_input.setPlaceholderText("Filas de la matriz")
        self.col_input.setPlaceholderText("Columnas de la matriz")

        self.size_button = QtWidgets.QPushButton("Crear matriz")
        self.size_button.clicked.connect(self.create_matrix_input)

        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()

        horizontal_layout1.addWidget(self.row_size)
        horizontal_layout1.addWidget(self.row_input)

        horizontal_layout2.addWidget(self.col_size)
        horizontal_layout2.addWidget(self.col_input)

        size_layout.addLayout(horizontal_layout1)
        size_layout.addLayout(horizontal_layout2)

        size_layout.addWidget(self.size_button)

        self.vbox.addLayout(size_layout)

        # Espacio para los campos de entrada de la matriz
        self.matrix_layout = QtWidgets.QGridLayout()
        self.matrix_widgets = []

        self.vbox.addLayout(self.matrix_layout)

        # Botón para obtener y mostrar la matriz
        self.get_matrix_A_button = QtWidgets.QPushButton("Guardar matriz A")
        self.get_matrix_A_button.clicked.connect(self.get_matrix_A)
        self.get_matrix_A_button.setDisabled(True)

        self.get_matrix_B_button = QtWidgets.QPushButton("Guardar matriz B")
        self.get_matrix_B_button.clicked.connect(self.get_matrix_B)
        self.get_matrix_B_button.setDisabled(True)

        self.sum_button = QtWidgets.QPushButton("Realizar suma")
        self.sum_button.clicked.connect(self.sum)

        self.subtraction_button = QtWidgets.QPushButton("Realizar resta")
        self.subtraction_button.clicked.connect(self.subtraction)

        self.vbox.addLayout(self.result_box)

        self.vbox.addWidget(self.get_matrix_A_button)
        self.vbox.addWidget(self.get_matrix_B_button)
        self.vbox.addWidget(self.sum_button)
        self.vbox.addWidget(self.subtraction_button)

        self.setLayout(self.vbox)
        self.setWindowTitle("Suma y resta de matrices")
        self.show()

    def create_matrix_input(self):
        row_size = int(self.row_input.text())
        col_size = int(self.col_input.text())
        self.actual_row_size = row_size
        self.actual_col_size = col_size

        # Limpia el layout anterior si existe
        for i in reversed(range(self.matrix_layout.count())):
            widget = self.matrix_layout.itemAt(i).widget()
            if widget is not None:
                self.matrix_layout.removeWidget(widget)
                widget.deleteLater()

        # Crear campos de entrada para la matriz cuadrada
        for i in range(row_size):
            row = []
            for j in range(col_size):
                line_edit = QtWidgets.QLineEdit()
                self.matrix_layout.addWidget(line_edit, i, j)
                row.append(line_edit)
            self.matrix_widgets.append(row)
        self.get_matrix_A_button.setDisabled(False)
        self.get_matrix_B_button.setDisabled(False)

    def get_matrix(self, state):
        matrix = []

        # Recopilar valores de los campos de entrada
        for row_widgets in self.matrix_widgets:
            row = []
            for widget in row_widgets:
                value = int(widget.text())
                row.append(value)
            matrix.append(row)

        # Aquí puedes almacenar la matriz en una variable o usarla para otros fines
        if state:
            print("Matriz A ingresada:")
            self.stored_matrix_A = matrix
        else:
            print("Matriz B ingresada:")
            self.stored_matrix_B = matrix
        for row in matrix:
            print(row)

    def get_matrix_A(self):
        self.get_matrix(True)

    def get_matrix_B(self):
        self.get_matrix(False)

    def sum(self):
        matrix_result = []
        process_matrix = []
        value = ''
        value_a = ''
        value_b = ''
        value_p = ''

        for i in range(self.actual_row_size):
            row = []
            process = []
            for j in range(self.actual_col_size):
                process.append(f'({self.stored_matrix_A[i][j]} + {self.stored_matrix_B[i][j]}) ')
                row.append(self.stored_matrix_A[i][j] + self.stored_matrix_B[i][j])

            matrix_result.append(row)
            process_matrix.append(process)

        for item in matrix_result:
            print(item)

        for row in self.stored_matrix_A:
            value_a += '|'
            for item in row:
                value_a += f'{item} '
            value_a += '| \n'
        value_a = value_a[: -1]

        for row in self.stored_matrix_B:
            value_b += '|'
            for item in row:
                value_b += f'{item} '
            value_b += '| \n'
        value_b = value_b[: -1]

        for row in process_matrix:
            value_p += '|'
            for item in row:
                value_p += f'{item} '
            value_p += '| \n'
        value_p = value_p[: -1]

        for row in matrix_result:
            value += '|'
            for item in row:
                value += f'{item} '
            value += '| \n'
        value = value[: -1]

        label1 = QLabel(f'El resultado de la suma es:')
        label2 = QLabel(f"{value_a}")
        label3 = QLabel('+')
        label4 = QLabel(f"{value_b}")
        label_equal = QLabel('=')
        label_equal1 = QLabel('=')
        label5 = QLabel(f"{value_p}")
        label6 = QLabel(f"{value}")

        # Vaciar el layout horizontal
        while self.result_box.count():
            item = self.result_box.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.result_box.addWidget(label1)
        self.result_box.addWidget(label2)
        self.result_box.addWidget(label3)
        self.result_box.addWidget(label4)
        self.result_box.addWidget(label_equal)
        self.result_box.addWidget(label5)
        self.result_box.addWidget(label_equal1)
        self.result_box.addWidget(label6)

    def subtraction(self):
        matrix_result = []
        process_matrix = []
        value = ''
        value_a = ''
        value_b = ''
        value_p = ''

        for i in range(self.actual_row_size):
            row = []
            process = []
            for j in range(self.actual_col_size):
                process.append(f'({self.stored_matrix_A[i][j]} - {self.stored_matrix_B[i][j]}) ')
                row.append(self.stored_matrix_A[i][j] - self.stored_matrix_B[i][j])

            matrix_result.append(row)
            process_matrix.append(process)

        for item in matrix_result:
            print(item)

        for row in self.stored_matrix_A:
            value_a += '|'
            for item in row:
                value_a += f'{item} '
            value_a += '| \n'
        value_a = value_a[: -1]

        for row in self.stored_matrix_B:
            value_b += '|'
            for item in row:
                value_b += f'{item} '
            value_b += '| \n'
        value_b = value_b[: -1]

        for row in process_matrix:
            value_p += '|'
            for item in row:
                value_p += f'{item} '
            value_p += '| \n'
        value_p = value_p[: -1]

        for row in matrix_result:
            value += '|'
            for item in row:
                value += f'{item} '
            value += '| \n'
        value = value[: -1]

        label1 = QLabel(f'El resultado de la resta es:')
        label2 = QLabel(f"{value_a}")
        label3 = QLabel('-')
        label4 = QLabel(f"{value_b}")
        label_equal = QLabel('=')
        label_equal1 = QLabel('=')
        label5 = QLabel(f"{value_p}")
        label6 = QLabel(f"{value}")

        # Vaciar el layout horizontal
        while self.result_box.count():
            item = self.result_box.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.result_box.addWidget(label1)
        self.result_box.addWidget(label2)
        self.result_box.addWidget(label3)
        self.result_box.addWidget(label4)
        self.result_box.addWidget(label_equal)
        self.result_box.addWidget(label5)
        self.result_box.addWidget(label_equal1)
        self.result_box.addWidget(label6)

    def closeEvent(self, event):
        self.close_window()
        event.accept()

    def close_window(self):
        self.close()
        self.app.setVisible(True)
