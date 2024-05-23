from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel, QSpinBox, QApplication, QMessageBox
import sys

class VectoresProductoPunto(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Producto Punto de Vectores')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.num_componentes_label = QLabel("Cantidad de Componentes por Vector:")
        self.num_componentes_input = QSpinBox()
        self.num_componentes_input.setMinimum(2)  # Al menos dos componentes
        self.num_componentes_input.setMaximum(10)  # Máximo diez componentes
        layout.addWidget(self.num_componentes_label)
        layout.addWidget(self.num_componentes_input)

        generate_button = QPushButton('Generar Vectores')
        generate_button.clicked.connect(self.generar_vectores)
        layout.addWidget(generate_button)

        self.vectores_layout = QVBoxLayout()
        layout.addLayout(self.vectores_layout)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        product_button = QPushButton('Calcular Producto Punto')
        product_button.clicked.connect(self.producto_punto)
        layout.addWidget(product_button)

        self.setLayout(layout)

    def generar_vectores(self):
        num_componentes = self.num_componentes_input.value()

        for i in reversed(range(self.vectores_layout.count())):
            widget = self.vectores_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        self.vectores = []
        for i in range(2):  # Siempre 2 vectores
            vector_layout = QVBoxLayout()
            vector_layout.addWidget(QLabel(f"Vector {chr(65 + i)}:"))
            componentes_layout = QHBoxLayout()
            componentes_edits = []
            for j in range(num_componentes):
                componente_edit = QLineEdit()
                componente_edit.setPlaceholderText(f"Componente {j+1}")
                componentes_layout.addWidget(componente_edit)
                componentes_edits.append(componente_edit)
            vector_layout.addLayout(componentes_layout)
            self.vectores_layout.addLayout(vector_layout)
            self.vectores.append(componentes_edits)

    def producto_punto(self):
        try:
            componentes_a = [float(edit.text()) for edit in self.vectores[0]]
            componentes_b = [float(edit.text()) for edit in self.vectores[1]]
            
            if len(componentes_a) != len(componentes_b):
                raise ValueError("Los vectores deben tener la misma cantidad de componentes.")

            dot_product = sum(a * b for a, b in zip(componentes_a, componentes_b))
            procedure = "Producto punto:\n"
            procedure += f"A: {componentes_a}\nB: {componentes_b}\n"
            procedure += " + ".join([f"({a} * {b})" for a, b in zip(componentes_a, componentes_b)])
            procedure += f" = {dot_product}"
            
            self.result_label.setText(procedure)
        except ValueError as e:
            QMessageBox.warning(self, "Entrada inválida", str(e))
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error: {str(e)}")


