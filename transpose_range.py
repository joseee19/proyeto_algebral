from PyQt5 import QtWidgets
import numpy as np
from PyQt5.QtWidgets import QMessageBox


class TransposeMatrixWindow(QtWidgets.QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setStyleSheet("background-color: #bcbcbc")
        self.stored_matrix = None
        self.initUI()

    def initUI(self):
        # Layout general
        vbox = QtWidgets.QVBoxLayout()

        # Layout para el tamaño de la matriz
        size_layout = QtWidgets.QHBoxLayout()
        self.rows_label = QtWidgets.QLabel("Ingrese el número de filas de la matriz:")
        self.cols_label = QtWidgets.QLabel("Ingrese el número de columnas de la matriz:")
        self.rows_input = QtWidgets.QLineEdit()
        self.cols_input = QtWidgets.QLineEdit()
        self.rows_input.setPlaceholderText("Filas de la matriz")
        self.cols_input.setPlaceholderText("Columnas de la matriz")
        self.size_button = QtWidgets.QPushButton("Crear matriz")
        self.size_button.clicked.connect(self.create_matrix_input)

        size_layout.addWidget(self.rows_label)
        size_layout.addWidget(self.rows_input)
        size_layout.addWidget(self.cols_label)
        size_layout.addWidget(self.cols_input)
        size_layout.addWidget(self.size_button)

        vbox.addLayout(size_layout)

        # Espacio para los campos de entrada de la matriz
        self.matrix_layout = QtWidgets.QGridLayout()
        self.matrix_widgets = []

        vbox.addLayout(self.matrix_layout)

        # Botones para obtener y mostrar la matriz, transpuesta y rango
        self.get_matrix_button = QtWidgets.QPushButton("Guardar matriz")
        self.get_matrix_button.clicked.connect(self.get_matrix)
        self.get_matrix_button.setDisabled(True)

        self.transpose_button = QtWidgets.QPushButton("Calcular transpuesta")
        self.transpose_button.clicked.connect(self.calculate_transpose)
        self.transpose_button.setDisabled(True)

        self.rank_button = QtWidgets.QPushButton("Calcular rango")
        self.rank_button.clicked.connect(self.calculate_rank)
        self.rank_button.setDisabled(True)

        vbox.addWidget(self.get_matrix_button)
        vbox.addWidget(self.transpose_button)
        vbox.addWidget(self.rank_button)

        self.setLayout(vbox)
        self.setWindowTitle("Operaciones con Matrices")
        self.show()

    def create_matrix_input(self):
        try:
            rows = int(self.rows_input.text())
            cols = int(self.cols_input.text())
        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, ingrese números enteros válidos para filas y columnas.")
            return

        self.matrix_widgets = []

        # Limpia el layout anterior si existe
        for i in reversed(range(self.matrix_layout.count())):
            widget = self.matrix_layout.itemAt(i).widget()
            if widget is not None:
                self.matrix_layout.removeWidget(widget)
                widget.deleteLater()

        # Crear campos de entrada para la matriz
        for i in range(rows):
            row = []
            for j in range(cols):
                line_edit = QtWidgets.QLineEdit()
                self.matrix_layout.addWidget(line_edit, i, j)
                row.append(line_edit)
            self.matrix_widgets.append(row)

        self.get_matrix_button.setDisabled(False)
        self.transpose_button.setDisabled(False)
        self.rank_button.setDisabled(False)

    def get_matrix(self):
        matrix = []

        # Recopilar valores de los campos de entrada
        try:
            for row_widgets in self.matrix_widgets:
                row = []
                for widget in row_widgets:
                    value = int(widget.text())
                    row.append(value)
                matrix.append(row)

            print("Matriz ingresada:")
            for row in matrix:
                print(row)

            self.stored_matrix = matrix
        except ValueError:
            QMessageBox.critical(self, "Error", "Por favor, ingrese solo números enteros en la matriz.")
            return

    def calculate_transpose(self):
        if self.stored_matrix is None:
            QMessageBox.critical(self, "Error", "Primero guarde la matriz ingresada.")
            return

        matrix = np.array(self.stored_matrix)
        transposed_matrix = np.transpose(matrix)

        transposed_str = "\n".join(["\t".join(map(str, row)) for row in transposed_matrix])
        QMessageBox.information(self, "Transpuesta de la matriz:", f"El resultado de la transpuesta es:\n{transposed_str}")

    def calculate_rank(self):
        if self.stored_matrix is None:
            QMessageBox.critical(self, "Error", "Primero guarde la matriz ingresada.")
            return

        matrix = np.array(self.stored_matrix)
        rank = np.linalg.matrix_rank(matrix)

        QMessageBox.information(self, "Rango de la matriz:", f"El rango de la matriz es:\n{rank}")

    def closeEvent(self, event):
        self.close_window()
        event.accept()

    def close_window(self):
        self.close()
        self.app.setVisible(True)
