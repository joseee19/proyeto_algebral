import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class VectoresDotProduct(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Producto Punto de Vectores')
        self.layout = QVBoxLayout()

        self.initUI()

        self.setLayout(self.layout)
        self.show()

    def initUI(self):
        self.vector_inputs_layout = QVBoxLayout()

        # Inputs for Vector A
        vector_a_layout = QHBoxLayout()
        vector_a_layout.addWidget(QLabel('Vector A:'))
        self.vector_a_x_input = QLineEdit()
        self.vector_a_x_input.setPlaceholderText('Componente x de A')
        self.vector_a_y_input = QLineEdit()
        self.vector_a_y_input.setPlaceholderText('Componente y de A')
        vector_a_layout.addWidget(self.vector_a_x_input)
        vector_a_layout.addWidget(self.vector_a_y_input)
        self.vector_inputs_layout.addLayout(vector_a_layout)

        # Inputs for Vector B
        vector_b_layout = QHBoxLayout()
        vector_b_layout.addWidget(QLabel('Vector B:'))
        self.vector_b_x_input = QLineEdit()
        self.vector_b_x_input.setPlaceholderText('Componente x de B')
        self.vector_b_y_input = QLineEdit()
        self.vector_b_y_input.setPlaceholderText('Componente y de B')
        vector_b_layout.addWidget(self.vector_b_x_input)
        vector_b_layout.addWidget(self.vector_b_y_input)
        self.vector_inputs_layout.addLayout(vector_b_layout)

        self.layout.addLayout(self.vector_inputs_layout)

        self.calculate_button = QPushButton('Calcular Producto Punto')
        self.calculate_button.clicked.connect(self.calculate_dot_product)
        self.layout.addWidget(self.calculate_button)

        self.result_label = QLabel('')
        self.layout.addWidget(self.result_label)

    def calculate_dot_product(self):
        try:
            ax = float(self.vector_a_x_input.text())
            ay = float(self.vector_a_y_input.text())
            bx = float(self.vector_b_x_input.text())
            by = float(self.vector_b_y_input.text())

            x_product = ax * bx
            y_product = ay * by
            dot_product = x_product + y_product

            result_text = (
                f"A({ax}, {ay}), B({bx}, {by})\n"
                f"A·B = ({ax} * {bx}) + ({ay} * {by}) = {x_product} + {y_product} = {dot_product}"
            )
            self.result_label.setText(f"Producto punto:\n{result_text}")
        except ValueError:
            QMessageBox.warning(self, "Entrada inválida", "Por favor, ingrese números válidos para los componentes de los vectores.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VectoresDotProduct()
    sys.exit(app.exec_())

