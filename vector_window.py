import sys
from PyQt5.QtWidgets import QApplication
from vector_sum import VectoresSum
from PyQt5.QtCore import Qt

class VectorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sum_vector_window = None
        self.setWindowTitle("Vectores")
        self.setFixedSize(800, 640)
        self.setStyleSheet("background-color: #bcbcbc")
        self.container = QWidget()
        self.initUI()

    def initUI(self):
        self.sum_button = QPushButton('Suma Vectores')
        self.sum_button.clicked.connect(self.ShowSumWindow)

        # Layout para la ventana principal
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.sum_button)

        # Crear un widget para el layout y establecerlo como central
        self.container.setLayout(main_layout)
        self.setCentralWidget(self.container)

    def ShowSumWindow(self):
        self.setVisible(False)  # Oculta la ventana principal
        self.sum_vector_window = VectoresSum(self)  # Instancia la ventana de suma de vectores
        self.sum_vector_window.setWindowModality(Qt.ApplicationModal)  # Hace que la ventana de suma sea modal
        self.sum_vector_window.show()  # Muestra la ventana de suma de vectores

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VectorWindow()
    window.show()
    sys.exit(app.exec_())
