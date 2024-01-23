import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("КРЕДИТНЫЙ КАЛЬКУЛЯТОР")





app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
