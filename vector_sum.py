import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel

class VectoresSum(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Suma de Vectores')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.vector1_layout = QHBoxLayout()
        self.vector1_label = QLabel('|A|')
        self.vector1_edit_x = QLineEdit()
        self.vector1_edit_y = QLineEdit()
        self.vector1_layout.addWidget(self.vector1_label)
        self.vector1_layout.addWidget(self.vector1_edit_x)
        self.vector1_layout.addWidget(self.vector1_edit_y)
        layout.addLayout(self.vector1_layout)

        self.vector2_layout = QHBoxLayout()
        self.vector2_label = QLabel('|B|')
        self.vector2_edit_x = QLineEdit()
        self.vector2_edit_y = QLineEdit()
        self.vector2_layout.addWidget(self.vector2_label)
        self.vector2_layout.addWidget(self.vector2_edit_x)
        self.vector2_layout.addWidget(self.vector2_edit_y)
        layout.addLayout(self.vector2_layout)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        sum_button = QPushButton('Sumar Vectores')
        sum_button.clicked.connect(self.sum_vectors)
        layout.addWidget(sum_button)

        self.setLayout(layout)

    def sum_vectors(self):
        try:
            vector1_x = float(self.vector1_edit_x.text())
            vector1_y = float(self.vector1_edit_y.text())

            vector2_x = float(self.vector2_edit_x.text())
            vector2_y = float(self.vector2_edit_y.text())

            result_x = vector1_x + vector2_x
            result_y = vector1_y + vector2_y

            self.result_label.setText(f"La suma es: ({result_x}, {result_y})")
        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VectoresSum()
    ex.show()
    sys.exit(app.exec_())
