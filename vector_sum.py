from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QSpinBox


class VectoresSum(QWidget):
    def __init__(self, app):
        super().__init__()
        self.setStyleSheet("background-color: #bcbcbc")
        self.initUI()
        self.app = app

    def initUI(self):
        self.setWindowTitle('Suma de Vectores')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.num_vectores_label = QLabel("Cantidad de Vectores:")
        self.num_vectores_input = QSpinBox()
        self.num_vectores_input.setMinimum(2)  # Al menos dos vectores
        self.num_vectores_input.setMaximum(10)  # Máximo diez vectores
        layout.addWidget(self.num_vectores_label)
        layout.addWidget(self.num_vectores_input)

        generate_button = QPushButton('Generar Vectores')
        generate_button.clicked.connect(self.generar_vectores)
        layout.addWidget(generate_button)

        self.vectores_layout = QVBoxLayout()

        layout.addLayout(self.vectores_layout)

        self.result_layout = QVBoxLayout()
        self.result_label = QLabel()
        self.result_layout.addWidget(self.result_label)
        layout.addLayout(self.result_layout)

        sum_button = QPushButton('Calcular Suma')
        sum_button.clicked.connect(self.calcular_suma)
        layout.addWidget(sum_button)

        self.setLayout(layout)

    def generar_vectores(self):
        # Limpiar el layout de vectores antes de generar nuevos vectores
        for i in reversed(range(self.vectores_layout.count())):
            widget = self.vectores_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        num_vectores = self.num_vectores_input.value()

        for i in range(num_vectores):
            vector_layout = QHBoxLayout()
            label = QLabel(f"Vector {chr(65 + i)}:")
            edit_x = QLineEdit()
            edit_y = QLineEdit()
            vector_layout.addWidget(label)
            vector_layout.addWidget(edit_x)
            vector_layout.addWidget(edit_y)
            self.vectores_layout.addLayout(vector_layout)

    def calcular_suma(self):
        num_vectores = self.num_vectores_input.value()

        try:
            suma_x = 0
            suma_y = 0
            procedure = "Suma de los vectores:\n"
            for i in range(num_vectores):
                vector_layout = self.vectores_layout.itemAt(i).layout()
                vector_x = float(vector_layout.itemAt(1).widget().text())
                vector_y = float(vector_layout.itemAt(2).widget().text())
                suma_x += vector_x
                suma_y += vector_y
                procedure += f"Vector {chr(65 + i)}: ({vector_x}, {vector_y})\n"

            procedure += f"\nResultado: ({suma_x}, {suma_y})"
            self.result_label.setText(procedure)

        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")

    def closeEvent(self, event):
        self.close_window()
        event.accept()

    def close_window(self):
        self.close()
        self.app.setVisible(True)
