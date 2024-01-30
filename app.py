import sys

from PyQt6.QtCore import Qt
from Credit_calculator import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget


class Calculator_app(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)



    def calculate_res():
        pass

    def calculate_paygraph():
        pass






def main():
    app = QApplication(sys.argv)
    window = Calculator_app()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()