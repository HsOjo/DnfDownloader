from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget

from ..view.MainWindow import Ui_MainWindow
from .C_MainWindow.DownloadPage import DownloadPage


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tw_content.addTab(DownloadPage(), 'Download')