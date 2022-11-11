from sys import argv

from PyQt6.QtWidgets import QApplication

from .controller.MainWindow import MainWindow


class Application:
    def __init__(self):
        self.qt = QApplication(argv)
        self.status = 0
        self.mw = MainWindow()

    def run(self):
        self.mw.show()
        self.status = self.qt.exec()
