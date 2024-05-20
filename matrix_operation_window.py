from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)
from sum_sub_window import SumSubMatrixWindow
from multiplication_window import MultiplicationMatrixWindow


class MatrixOperationWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.sum_window = None
        self.multiplication_window = None
        self.setWindowTitle("Operaciones entre matrices")
        self.setFixedSize(640, 480)
        self.setStyleSheet("background-color: #bcbcbc")
        self.container = QWidget()
        self.initUI()

    def initUI(self):
        # Layout para la ventana principal
        main_layout = QVBoxLayout()
        sum_matrix_button = QPushButton("Suma y resta")
        multiplication_matrix_button = QPushButton("Multiplicación")
        close_button = QPushButton("Volver")
        close_button.setFixedSize(80, 30)

        sum_matrix_button.clicked.connect(self.show_sum_window)
        multiplication_matrix_button.clicked.connect(self.show_multiplication_window)
        close_button.clicked.connect(self.close_window)

        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()

        horizontal_layout1.addWidget(sum_matrix_button)
        horizontal_layout1.addWidget(multiplication_matrix_button)

        horizontal_layout2.addWidget(close_button)

        # Crear un widget para el layout y establecerlo como central
        main_layout.addLayout(horizontal_layout1)
        main_layout.addLayout(horizontal_layout2)

        self.container.setLayout(main_layout)
        self.setCentralWidget(self.container)

    def show_sum_window(self):
        self.setVisible(False)
        self.sum_window = SumSubMatrixWindow(self)
        self.sum_window.show()

    def show_multiplication_window(self):
        self.setVisible(False)
        self.multiplication_window = MultiplicationMatrixWindow(self)
        self.multiplication_window.show()

    def closeEvent(self, event):
        self.close_window()
        event.accept()

    def close_window(self):
        self.close()
        self.app.setVisible(True)
