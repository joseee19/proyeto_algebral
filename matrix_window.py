from matrix_operation_window import MatrixOperationWindow
from inverse_matrix_window import InverseMatrixWindow
from matrix_determinant_window import DeterminantWindow
from transpose_range import TransposeMatrixWindow
from matrix_cifrate import EncryptionWindow
from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget
)


class MatrixWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Matrices")
        self.setFixedSize(640, 480)
        self.setStyleSheet("background-color: #bcbcbc")
        self.matrix_operation_window = None
        self.inverse_matrix_window = None
        self.determinant_window = None
        self.transpose_window = None
        self.encryption_window = None
        self.container = QWidget()
        self.initUI()

    def initUI(self):

        # Layout para la ventana principal
        main_layout = QVBoxLayout()
        operations_button = QPushButton("Operaciones entre matrices")
        inverse_matrix_button = QPushButton("Matriz inversa")
        matrix_determinant_button = QPushButton("Determinante de matriz")
        matrix_range_button = QPushButton("Rango y transpuesta de una matriz")
        matrix_encryption = QPushButton("Cifrar mensaje")
        markov_chain = QPushButton("Cadena de Markov")
        close_button = QPushButton("Volver")

        close_button.setFixedSize(80, 30)

        operations_button.clicked.connect(self.show_mtx_op_wndw)
        inverse_matrix_button.clicked.connect(self.show_inverse_matrix_wndw)
        matrix_determinant_button.clicked.connect(self.show_determinant_window)
        matrix_range_button.clicked.connect(self.show_transpose_window)
        matrix_encryption.clicked.connect(self.show_encryption_window)
        close_button.clicked.connect(self.close_window)

        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()
        horizontal_layout3 = QHBoxLayout()

        horizontal_layout1.addWidget(operations_button)
        horizontal_layout1.addWidget(inverse_matrix_button)
        horizontal_layout1.addWidget(matrix_determinant_button)

        horizontal_layout2.addWidget(matrix_range_button)
        horizontal_layout2.addWidget(matrix_encryption)
        horizontal_layout2.addWidget(markov_chain)

        horizontal_layout3.addWidget(close_button)

        # Crear un widget para el layout y establecerlo como central
        main_layout.addLayout(horizontal_layout1)
        main_layout.addLayout(horizontal_layout2)
        main_layout.addLayout(horizontal_layout3)

        self.container.setLayout(main_layout)
        self.setCentralWidget(self.container)

    def show_mtx_op_wndw(self):
        self.setVisible(False)
        self.matrix_operation_window = MatrixOperationWindow(self)
        self.matrix_operation_window.show()

    def show_inverse_matrix_wndw(self):
        self.setVisible(False)
        self.inverse_matrix_window = InverseMatrixWindow(self)
        self.inverse_matrix_window.show()

    def show_determinant_window(self):
        self.setVisible(False)
        self.determinant_window = DeterminantWindow(self)
        self.determinant_window.show()

    def show_transpose_window(self):
        self.setVisible(False)
        self.transpose_window = TransposeMatrixWindow(self)
        self.transpose_window.show()

    def show_encryption_window(self):
        self.setVisible(False)
        self.encryption_window = EncryptionWindow(self)
        self.encryption_window.show()

    def closeEvent(self, event):
        self.close_window()
        event.accept()

    def close_window(self):
        self.close()
        self.app.setVisible(True)
