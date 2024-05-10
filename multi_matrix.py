import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout


class MatrixMultiplication(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Multiplicación de Matrices')
        self.setGeometry(100, 100, 300, 200)

        self.rows1_label = QLabel('Filas Matriz 1:')
        self.rows1_input = QLineEdit()
        self.cols1_label = QLabel('Columnas Matriz 1:')
        self.cols1_input = QLineEdit()
        self.rows2_label = QLabel('Filas Matriz 2:')
        self.rows2_input = QLineEdit()
        self.cols2_label = QLabel('Columnas Matriz 2:')
        self.cols2_input = QLineEdit()

        self.create_matrix_button = QPushButton('Crear Matrices')
        self.create_matrix_button.clicked.connect(self.create_matrices_input)

        self.matrix1_label = QLabel('Primera Matriz:')
        self.matrix2_label = QLabel('Segunda Matriz:')
        self.result_label = QLabel('Resultado:')
        self.result_output = QLineEdit()
        self.result_output.setReadOnly(True)

        self.multiply_button = QPushButton('Multiplicar')
        self.multiply_button.clicked.connect(self.multiply_matrices)
        self.multiply_button.setDisabled(True)

        layout = QVBoxLayout()
        layout.addWidget(self.rows1_label)
        layout.addWidget(self.rows1_input)
        layout.addWidget(self.cols1_label)
        layout.addWidget(self.cols1_input)
        layout.addWidget(self.rows2_label)
        layout.addWidget(self.rows2_input)
        layout.addWidget(self.cols2_label)
        layout.addWidget(self.cols2_input)
        layout.addWidget(self.create_matrix_button)
        layout.addWidget(self.matrix1_label)
        layout.addWidget(self.matrix2_label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_output)
        layout.addWidget(self.multiply_button)

        self.setLayout(layout)

    def create_matrices_input(self):
        rows1 = int(self.rows1_input.text())
        cols1 = int(self.cols1_input.text())
        rows2 = int(self.rows2_input.text())
        cols2 = int(self.cols2_input.text())

        if cols1 != rows2:
            self.result_output.setText('Error: No se pueden multiplicar matrices con estas dimensiones.')
            return

        self.matrix1_input = [[QLineEdit() for _ in range(cols1)] for _ in range(rows1)]
        self.matrix2_input = [[QLineEdit() for _ in range(cols2)] for _ in range(rows2)]

        # Setup layout for matrices
        matrix_layout = QGridLayout()
        for i in range(rows1):
            for j in range(cols1):
                matrix_layout.addWidget(self.matrix1_input[i][j], i, j)
        for i in range(rows2):
            for j in range(cols2):
                matrix_layout.addWidget(self.matrix2_input[i][j], i + rows1 + 1, j)
        self.matrix1_label.show()
        self.matrix2_label.show()
        self.result_label.show()
        self.result_output.show()
        self.multiply_button.setDisabled(False)

        layout = self.layout()
        layout.addLayout(matrix_layout)

    def multiply_matrices(self):
        rows1 = len(self.matrix1_input)
        cols1 = len(self.matrix1_input[0])
        rows2 = len(self.matrix2_input)
        cols2 = len(self.matrix2_input[0])

        try:
            matrix1 = [[int(self.matrix1_input[i][j].text()) for j in range(cols1)] for i in range(rows1)]
            matrix2 = [[int(self.matrix2_input[i][j].text()) for j in range(cols2)] for i in range(rows2)]

            result_matrix = [[0 for _ in range(cols2)] for _ in range(rows1)]

            for i in range(rows1):
                for j in range(cols2):
                    for k in range(cols1):
                        result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

            result_text = '\n'.join(' '.join(str(cell) for cell in row) for row in result_matrix)
            self.result_output.setText(result_text)
        except ValueError:
            self.result_output.setText('Error: Ingrese matrices válidas (números enteros).')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MatrixMultiplication()
    window.show()
    sys.exit(app.exec_())