import sys
from PyQt5.QtWidgets import QApplication
from mainwindow import MainWindow


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow(app)
    main_window.show()
    sys.exit(app.exec())


main()
