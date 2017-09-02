from os import makedirs, unlink

from PyQt5.QtCore import QThread, pyqtSignal

from lib.Download import Download
from lib.spk import spk
from ...common import *
from ...config import Config


class TDownload(QThread):
    p_s_signal = pyqtSignal(int, int)
    p_g_signal = pyqtSignal(int, int)
    i_signal = pyqtSignal(str, str)
    sp_signal = pyqtSignal(str)
    fin_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.src = ''
        self.d_list = []
        self.downer = Download()
        self.downer.event_connect('progress', self._cb_progress)
        self.downer.event_connect('start', self._cb_start)
        self.downer.event_connect('error', print)
        self.f_now = ''

    def setArgs(self, **kwargs):
        self.src = kwargs['src']
        self.d_list = list(reversed(kwargs['d_list']))

    def run(self):
        l = len(self.d_list)
        for i in range(l):
            f = self.d_list[i]
            self.f_now = f + '.spk'

            p = '%s/%s' % (Config.down_dir, self.f_now)
            makedirs(getdirectory(p), exist_ok=True)

            self.downer.download(self.src + self.f_now, p)
            if spk(p).unpack(p[:-4]):
                unlink(p)

            self.p_g_signal.emit(i, l - 1)
            self.fin_signal.emit(f)

    def _cb_progress(self, a_size, n_size, s_time, n_time):
        self.p_s_signal.emit(n_size, a_size)
        self.sp_signal.emit(str(n_size // (n_time - s_time) // 1024) + 'kb/s')

    def _cb_start(self, header):
        # print(header)
        f_size = str(int(header['Content-Length']) // 1024) + 'kb'
        self.i_signal.emit(self.f_now, f_size)
