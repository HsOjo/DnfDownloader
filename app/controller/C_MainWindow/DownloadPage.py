from PyQt5.QtWidgets import QWidget

from ...common import *
from ...config import Config
from ...model.FileList import FileList
from ...view.C_MainWindow.DownloadPage import Ui_DownloadPage


class DownloadPage(Ui_DownloadPage, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model_fl = FileList()

        self.data_fl = []
        self.data_dl = []

        for src in Config.source:
            self.cb_src.addItem(src)

        self.pb_update_fl.clicked.connect(self._pb_update_fl_clicked)
        self.pb_search_fl.clicked.connect(self._pb_search_fl_clicked)
        self.pb_add_dl.clicked.connect(self._pb_add_dl_clicked)
        self.pb_drop_dl.clicked.connect(self._pb_drop_dl_clicked)
        self.pb_clear_dl.clicked.connect(self._pb_clear_dl_clicked)

    def view_file_list(self, data):
        old_row = self.lw_file_l.currentRow()
        self.lw_file_l.clear()
        self.lw_file_l.addItems(list_reduce(data, self.data_dl))
        self.lw_file_l.setCurrentRow(old_row)

    def _pb_update_fl_clicked(self):
        src = self.cb_src.currentText()
        self.model_fl.update(src)
        self.data_fl = self.model_fl.data
        self.view_file_list(self.data_fl)
        self.le_search_fl.setText('')

    def _pb_search_fl_clicked(self):
        keyword = self.le_search_fl.text()
        if keyword != '':
            self.data_fl = self.model_fl.search(keyword)
            self.view_file_list(self.data_fl)
        else:
            self.view_file_list(self.model_fl.data)

    def _pb_add_dl_clicked(self):
        data = []
        sels = self.lw_file_l.selectedIndexes()  # type: list
        sels.sort(key=lambda x: x.row())
        for i in range(len(sels) - 1, -1, -1):
            sel = self.lw_file_l.takeItem(sels[i].row())
            istr = sel.text()
            data.insert(0, istr)
            self.data_dl.append(istr)
        self.lw_down_l.addItems(data)

    def _pb_drop_dl_clicked(self):
        data = []
        sels = self.lw_down_l.selectedIndexes()
        sels.sort(key=lambda x: x.row())
        for i in range(len(sels) - 1, -1, -1):
            sel = self.lw_down_l.takeItem(sels[i].row())
            istr = sel.text()
            if istr in self.data_fl:
                data.insert(0, istr)
            self.data_dl.remove(istr)
        self.lw_file_l.addItems(data)

    def _pb_clear_dl_clicked(self):
        data = []
        for i in range(len(self.data_dl) - 1, -1, -1):
            istr = self.data_dl.pop(i)
            if istr in self.data_fl:
                data.insert(0, istr)
        self.lw_down_l.clear()
        self.lw_file_l.addItems(data)
