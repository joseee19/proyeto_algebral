import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout


class MatrixSum(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Suma de Matrices')
        self.setGeometry(100, 100, 300, 200)

        self.rows_label = QLabel('Número de filas:')
        self.rows_input = QLineEdit()
        self.cols_label = QLabel('Número de columnas:')
        self.cols_input = QLineEdit()

        self.create_matrix_button = QPushButton('Crear Matrices')
        self.create_matrix_button.clicked.connect(self.create_matrices_input)

        self.matrix1_label = QLabel('Primera Matriz:')
        self.matrix2_label = QLabel('Segunda Matriz:')
        self.result_label = QLabel('Resultado:')
        self.result_output = QLineEdit()
        self.result_output.setReadOnly(True)

        self.sum_button = QPushButton('Sumar')
        self.sum_button.clicked.connect(self.sum_matrices)
        self.sum_button.setDisabled(True)

        layout = QVBoxLayout()
        layout.addWidget(self.rows_label)
        layout.addWidget(self.rows_input)
        layout.addWidget(self.cols_label)
        layout.addWidget(self.cols_input)
        layout.addWidget(self.create_matrix_button)
        layout.addWidget(self.matrix1_label)
        layout.addWidget(self.matrix2_label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_output)
        layout.addWidget(self.sum_button)

        self.setLayout(layout)

    def create_matrices_input(self):
        rows = int(self.rows_input.text())
        cols = int(self.cols_input.text())

        self.matrix1_input = [[QLineEdit() for _ in range(cols)] for _ in range(rows)]
        self.matrix2_input = [[QLineEdit() for _ in range(cols)] for _ in range(rows)]

        # Setup layout for matrices
        matrix_layout = QGridLayout()
        for i in range(rows):
            for j in range(cols):
                matrix_layout.addWidget(self.matrix1_input[i][j], i, j)
                matrix_layout.addWidget(self.matrix2_input[i][j], i + rows + 1, j)
        self.matrix1_label.show()
        self.matrix2_label.show()
        self.result_label.show()
        self.result_output.show()
        self.sum_button.setDisabled(False)

        layout = self.layout()
        layout.addLayout(matrix_layout)

    def sum_matrices(self):
        rows = len(self.matrix1_input)
        cols = len(self.matrix1_input[0])

        # Parse input matrices
        try:
            matrix1 = [[int(self.matrix1_input[i][j].text()) for j in range(cols)] for i in range(rows)]
            matrix2 = [[int(self.matrix2_input[i][j].text()) for j in range(cols)] for i in range(rows)]

            result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

            result_text = '\n'.join(' '.join(str(cell) for cell in row) for row in result_matrix)
            self.result_output.setText(result_text)
        except ValueError:
            self.result_output.setText('Error: Ingrese matrices válidas (números enteros).')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MatrixSum()
    window.show()
    sys.exit(app.exec_())