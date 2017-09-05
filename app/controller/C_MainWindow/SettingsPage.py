from PyQt5.QtWidgets import QWidget, QFileDialog

from ...config import Config
from ...view.C_MainWindow.SettingsPage import Ui_SettingsPage


class SettingsPage(Ui_SettingsPage, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.le_dd.setText(Config.down_dir)
        self.le_bs.setText(str(Config.block_size))
        self.le_retry.setText(str(Config.retry_count))

        self.tb_dd.clicked.connect(self._tb_dd_clicked)
        self.pb_apply.clicked.connect(self._pb_apply_clicked)

    def _tb_dd_clicked(self):
        d = QFileDialog.getExistingDirectory(self, 'Select download directory.')
        self.le_dd.setText(d)

    def _pb_apply_clicked(self):
        Config.down_dir = self.le_dd.text()
        Config.block_size = int(self.le_bs.text())
        Config.retry_count = int(self.le_retry.text())