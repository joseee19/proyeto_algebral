from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


class VectorWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Vectores")
        self.setFixedSize(800, 640)
        self.setStyleSheet("background-color: #bcbcbc")
        self.container = QWidget()
        self.initUI()

    def initUI(self):

        # Layout para la ventana principal
        main_layout = QVBoxLayout()

        # Crear un widget para el layout y establecerlo como central
        self.container.setLayout(main_layout)
        self.setCentralWidget(self.container)
