import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGridLayout


class MatrixSum(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Suma de Matrices')
        self.setGeometry(100, 100, 300, 200)

        self.size_label = QLabel('Tamaño de la matriz:')
        self.size_input = QLineEdit()
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
        layout.addWidget(self.size_label)
        layout.addWidget(self.size_input)
        layout.addWidget(self.create_matrix_button)
        layout.addWidget(self.matrix1_label)
        layout.addWidget(self.matrix2_label)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_output)
        layout.addWidget(self.sum_button)

        self.setLayout(layout)

    def create_matrices_input(self):
        size = int(self.size_input.text())
        self.matrix1_input = [[QLineEdit() for _ in range(size)] for _ in range(size)]
        self.matrix2_input = [[QLineEdit() for _ in range(size)] for _ in range(size)]

        # Setup layout for matrices
        matrix_layout = QGridLayout()
        for i in range(size):
            for j in range(size):
                matrix_layout.addWidget(self.matrix1_input[i][j], i, j)
                matrix_layout.addWidget(self.matrix2_input[i][j], i + size + 1, j)
        self.matrix1_label.show()
        self.matrix2_label.show()
        self.result_label.show()
        self.result_output.show()
        self.sum_button.setDisabled(False)

        layout = self.layout()
        layout.addLayout(matrix_layout)

    def sum_matrices(self):
        size = len(self.matrix1_input)

        # Parse input matrices
        try:
            matrix1 = [[int(self.matrix1_input[i][j].text()) for j in range(size)] for i in range(size)]
            matrix2 = [[int(self.matrix2_input[i][j].text()) for j in range(size)] for i in range(size)]

            result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(size)] for i in range(size)]

            result_text = '\n'.join(' '.join(str(cell) for cell in row) for row in result_matrix)
            self.result_output.setText(result_text)
        except ValueError:
            self.result_output.setText('Error: Ingrese matrices válidas (números enteros).')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MatrixSum()
    window.show()
    sys.exit(app.exec_())

