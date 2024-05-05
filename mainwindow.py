import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from matrix_window import MatrixWindow
from vector_window import VectorWindow


class MainWindow(QMainWindow):
    def __init__(self, app):

        super().__init__()
        self.vector_window = None
        self.matrix_window = None
        self.app = app

        self.setFixedSize(640, 480)
        self.setWindowTitle("Proyecto álgebra lineal")

        # Creamos un widget central para la ventana principal
        widget_central = QWidget()
        widget_central.setStyleSheet("background-color: #E0EBFF")

        # Creamos un layout horizontal que contendrá a los dos verticales
        layout_horizontal_main = QHBoxLayout()
        layout_vertical_left = QVBoxLayout()
        layout_vertical_right = QVBoxLayout()
        # Creamos los botones correspondientes para cada estructura y ajustamos su tamaño.
        boton_1 = QPushButton("Matrices")
        boton_1.setFixedSize(130, 40)
        boton_1.setStyleSheet("background-color: #bcbcbc")
        boton_2 = QPushButton("Vectores")
        boton_2.setFixedSize(130, 40)
        boton_2.setStyleSheet("background-color: #bcbcbc")

        boton_3 = QPushButton("Cerrar")
        boton_3.setFixedSize(80, 30)
        boton_3.setStyleSheet("background-color: #bcbcbb")

        # Creamos un layout horizontal auxiliar para centrar los botones.
        layout_horizontal1 = QHBoxLayout()
        layout_horizontal2 = QHBoxLayout()
        layout_vertical1 = QVBoxLayout()
        layout_vertical2 = QVBoxLayout()

        # Añadimos los botones al layout horizontal.
        layout_vertical1.addWidget(boton_1)
        layout_vertical1.setAlignment(Qt.AlignHCenter)
        layout_vertical2.addWidget(boton_2)
        layout_vertical2.setAlignment(Qt.AlignHCenter)

        layout_horizontal1.addLayout(layout_vertical1)
        layout_horizontal1.addLayout(layout_vertical2)
        layout_horizontal2.addWidget(boton_3)

        # **Centramos los botones horizontalmente.**
        layout_horizontal1.setAlignment(Qt.AlignHCenter)
        layout_horizontal2.setAlignment(Qt.AlignHCenter)

        # Añadimos los layouts horizontales a los layouts verticales.
        layout_vertical_left.addLayout(layout_horizontal1)
        layout_vertical_left.addLayout(layout_horizontal2)

        # Establecemos el layout horizontal como el layout del widget central

        layout_horizontal_main.addLayout(layout_vertical_left)
        widget_central.setLayout(layout_horizontal_main)

        # Establecemos el widget central como el widget principal de la ventana
        self.setCentralWidget(widget_central)

        # Conectamos los botones a las funciones para abrir las otras ventanas
        boton_1.clicked.connect(self.show_matrix_window)
        boton_2.clicked.connect(self.show_vector_window)
        boton_3.clicked.connect(self.close_program)

    # Funciones para mostrar cada ventana
    def show_vector_window(self):
        self.vector_window = VectorWindow(self.app)
        self.vector_window.show()
        while True:
            self.app.processEvents()

    def show_matrix_window(self):
        self.setVisible(False)
        self.matrix_window = MatrixWindow(self)
        self.matrix_window.show()
        while True:
            self.app.processEvents()

    def close_program(self):
        sys.exit(self.app.exec())
