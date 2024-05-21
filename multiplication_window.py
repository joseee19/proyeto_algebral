from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QVBoxLayout, QMessageBox


class MultiplicationMatrixWindow(QtWidgets.QWidget):
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

        self.multiplication_button = QtWidgets.QPushButton("Realizar multiplicación")
        self.multiplication_button.clicked.connect(self.multiplication)

        self.vbox.addLayout(self.result_box)

        self.vbox.addWidget(self.get_matrix_A_button)
        self.vbox.addWidget(self.get_matrix_B_button)
        self.vbox.addWidget(self.multiplication_button)

        self.setLayout(self.vbox)
        self.setWindowTitle("Multiplicación de matrices")
        self.show()

    def create_matrix_input(self):
        # Get the number of rows and columns from input fields
        row_size = int(self.row_input.text())
        col_size = int(self.col_input.text())
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
        # Enable buttons to get matrices
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

    def multiplication(self):
        if self.stored_matrix_A is None or self.stored_matrix_B is None:
            QMessageBox.critical(self, "Error", "Por favor, guarde ambas matrices antes de realizar la multiplicación.")
            return

        rows_a, cols_a = len(self.stored_matrix_A), len(self.stored_matrix_A[0])
        rows_b, cols_b = len(self.stored_matrix_B), len(self.stored_matrix_B[0])

        if cols_a != rows_b:
            QMessageBox.critical(self, "Error",
                                 "Las columnas de la matriz A y las filas de la matriz B no son iguales.")
            return

        matrix_result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        process_matrix = [["" for _ in range(cols_b)] for _ in range(rows_a)]

        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    process_matrix[i][j] += f" {self.stored_matrix_A[i][k]} * {self.stored_matrix_B[k][j]} + "
                    matrix_result[i][j] += self.stored_matrix_A[i][k] * self.stored_matrix_B[k][j]
                process_matrix[i][j] = process_matrix[i][j].strip(" + ")

        value_a = self.format_matrix(self.stored_matrix_A)
        value_b = self.format_matrix(self.stored_matrix_B)
        value_p = self.format_matrix(process_matrix, is_process=True)
        value_result = self.format_matrix(matrix_result)

        self.display_result(value_a, value_b, value_p, value_result)

    def format_matrix(self, matrix, is_process=False):
        formatted = ""
        for row in matrix:
            formatted += "|"
            for item in row:
                formatted += f"{item} " if is_process else f"{item} "
            formatted += "|\n"
        return formatted.strip()

    def display_result(self, value_a, value_b, value_p, value_result):
        self.clear_layout()

        self.result_box.addWidget(QLabel('El resultado de la multiplicación es:'))
        self.result_box.addWidget(QLabel(f"{value_a}"))
        self.result_box.addWidget(QLabel('*'))
        self.result_box.addWidget(QLabel(f"{value_b}"))
        self.result_box.addWidget(QLabel('='))
        self.result_box.addWidget(QLabel(f"{value_p}"))
        self.result_box.addWidget(QLabel('='))
        self.result_box.addWidget(QLabel(f"{value_result}"))

    def clear_layout(self):
        while self.result_box.count():
            item = self.result_box.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def closeEvent(self, event):
        self.close_window()
        event.accept()

    def close_window(self):
        self.close()
        self.app.setVisible(True)
