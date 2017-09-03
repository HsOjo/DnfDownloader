from PyQt5.QtWidgets import QWidget, QListWidget

from ...common import *
from ...config import Config
from ...model.FileList import FileList
from ...thread.MainWindow.TDownload import TDownload
from ...view.C_MainWindow.DownloadPage import Ui_DownloadPage


class DownloadPage(Ui_DownloadPage, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model_fl = FileList()

        self.src = ''
        self.data_fl = []
        self.data_fl_v = []
        self.data_dl = []
        self.data_fin = []

        self.t_down = TDownload()
        self.t_down.p_s_signal.connect(self._t_cb_update_s_progress)
        self.t_down.p_g_signal.connect(self._t_cb_update_g_progress)
        self.t_down.i_signal.connect(self._t_cb_update_info)
        self.t_down.sp_signal.connect(self._t_cb_update_speed)
        self.t_down.fin_signal.connect(self._t_cb_finish_file)

        self.pb_sp.setValue(0)
        self.pb_gp.setValue(0)

        for src in Config.source.keys():
            self.cb_src.addItem(src)

        self.pb_update_fl.clicked.connect(self._pb_update_fl_clicked)
        self.pb_search_fl.clicked.connect(self._pb_search_fl_clicked)
        self.pb_add_dl.clicked.connect(self._pb_add_dl_clicked)
        self.pb_drop_dl.clicked.connect(self._pb_drop_dl_clicked)
        self.pb_clear_dl.clicked.connect(self._pb_clear_dl_clicked)
        self.pb_down.clicked.connect(self._pb_down_clicked)

    def set_file_list(self, data):
        old_row = self.lw_file_l.currentRow()
        self.lw_file_l.clear()
        data = list_reduce(data, self.data_dl)
        data = list_reduce(data, self.data_fin)
        self.lw_file_l.addItems(data)
        self.lw_file_l.setCurrentRow(old_row)

    def _pb_update_fl_clicked(self):
        src = self.cb_src.currentText()
        self.model_fl.update(src)
        self.src = src

        data = self.model_fl.data
        if self.model_fl.data:
            self.data_fl = data
            self.data_fl_v = self.data_fl
            self.set_file_list(self.data_fl_v)
            self.le_search_fl.setText('')

    def _pb_search_fl_clicked(self):
        keyword = self.le_search_fl.text()
        if keyword != '':
            self.data_fl_v = self.model_fl.search(keyword)
            self.set_file_list(self.data_fl_v)
        else:
            self.set_file_list(self.data_fl)

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
            if istr in self.data_fl_v:
                data.insert(0, istr)
            self.data_dl.remove(istr)
        self.lw_file_l.addItems(data)

    def _pb_clear_dl_clicked(self):
        data = []
        for i in range(len(self.data_dl) - 1, -1, -1):
            istr = self.data_dl.pop(i)
            if istr in self.data_fl_v:
                data.insert(0, istr)
        self.lw_down_l.clear()
        self.lw_file_l.addItems(data)

    def _pb_down_clicked(self):
        self.pb_down.setEnabled(False)
        self.l_source.setText(self.src)
        self.t_down.set_args(src=self.src, d_list=self.data_dl)
        self.t_down.start()

    def _t_cb_update_s_progress(self, now, max):
        self.pb_sp.setValue(now)
        self.pb_sp.setMaximum(max)

    def _t_cb_update_g_progress(self, now, max):
        self.pb_gp.setValue(now)
        self.pb_gp.setMaximum(max)
        if now == max:
            self.pb_down.setEnabled(True)

    def _t_cb_update_info(self, f_name, f_size):
        self.l_f_name.setText(getfilename(f_name))
        self.l_f_size.setText(f_size)

    def _t_cb_update_speed(self, speed):
        self.l_speed.setText(speed)

    def _t_cb_finish_file(self, filename):
        def list_item_remove(list: QListWidget, item_str):
            for r in range(list.count() - 1, -1, -1):
                if list.item(r).text() == item_str:
                    list.takeItem(r)

        list_item_remove(self.lw_file_l, filename)
        list_item_remove(self.lw_down_l, filename)

        if filename in self.data_dl:
            self.data_dl.remove(filename)
        self.data_fin.append(filename)
