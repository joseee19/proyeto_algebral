from matrix_operation_window import MatrixOperationWindow
from inverse_matrix_window import InverseMatrixWindow
from vector_sum import VectoresSum
from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget
)


class VectorWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Vectores")
        self.setFixedSize(640, 480)
        self.setStyleSheet("background-color: #bcbcbc")
        self.vector_sum_window = None
        self.container = QWidget()
        self.initUI()

    def initUI(self):

        # Layout para la ventana principal
        main_layout = QVBoxLayout()
        sum_vector_button = QPushButton("Suma de vectores")
        vector_product = QPushButton("Producto punto de vectores")
        close_button = QPushButton("Volver")

        close_button.setFixedSize(80, 30)

        sum_vector_button.clicked.connect(self.show_vector_sum_window)
        close_button.clicked.connect(self.close_window)

        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()
        horizontal_layout3 = QHBoxLayout()

        horizontal_layout1.addWidget(sum_vector_button)

        horizontal_layout2.addWidget(vector_product)

        horizontal_layout3.addWidget(close_button)

        # Crear un widget para el layout y establecerlo como central
        main_layout.addLayout(horizontal_layout1)
        main_layout.addLayout(horizontal_layout2)
        main_layout.addLayout(horizontal_layout3)

        self.container.setLayout(main_layout)
        self.setCentralWidget(self.container)

    def show_vector_sum_window(self):
        self.setVisible(False)
        self.vector_sum_window = VectoresSum(self)
        self.vector_sum_window.show()

    def closeEvent(self, event):
        self.close_window()
        event.accept()

    def close_window(self):
        self.close()
        self.app.setVisible(True)
