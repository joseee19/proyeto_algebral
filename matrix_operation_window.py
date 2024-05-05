from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


class MatrixOperationWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Operaciones entre matrices")
        self.setFixedSize(640, 480)
        self.setStyleSheet("background-color: #bcbcbc")
        self.container = QWidget()
        self.initUI()

    def initUI(self):
        # Layout para la ventana principal
        main_layout = QVBoxLayout()
        sum_matrix_button = QPushButton("Suma")
        substraction_matrix_button = QPushButton("Resta")
        multiplication_matrix_button = QPushButton("Multiplicación")
        close_button = QPushButton("Volver")

        close_button.clicked.connect(self.close_window)

        horizontal_layout1 = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()

        horizontal_layout1.addWidget(sum_matrix_button)
        horizontal_layout1.addWidget(substraction_matrix_button)
        horizontal_layout1.addWidget(multiplication_matrix_button)

        horizontal_layout2.addWidget(close_button)

        # Crear un widget para el layout y establecerlo como central
        main_layout.addLayout(horizontal_layout1)
        main_layout.addLayout(horizontal_layout2)

        self.container.setLayout(main_layout)
        self.setCentralWidget(self.container)

    def closeEvent(self, event):
        self.close_window()
        event.accept()

    def close_window(self):
        self.close()
        self.app.setVisible(True)
