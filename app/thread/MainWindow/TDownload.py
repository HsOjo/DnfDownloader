from os import makedirs, unlink

from PyQt5.QtCore import QThread, pyqtSignal

from lib.Download import Download
from lib.SPK import SPK
from lib.TCT import TCT
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
        self.fmt = ''
        self.e_name = ''

        self.d_list = []
        self.downer = Download()
        self.downer.event_connect('progress', self._cb_progress)
        self.downer.event_connect('start', self._cb_start)
        self.downer.event_connect('error', print)
        self.f_now = ''

    def set_args(self, **kwargs):
        self.src = kwargs['src']
        info = Config.source[self.src]
        self.fmt = info['format']
        self.e_name = '.%s' % self.fmt
        self.d_list = list(reversed(kwargs['d_list']))

    def run(self):
        l = len(self.d_list)
        for i in range(l):
            f = self.d_list[i]
            self.f_now = f + self.e_name

            p = '%s/%s' % (Config.down_dir, self.f_now)
            makedirs(getdirectory(p), exist_ok=True)

            down_fin = False
            for x in range(Config.retry_count + 1):
                if x > 0:
                    print(p, 'retry:%s' % x)
                down_fin = self.downer.download(self.src + self.f_now, p)
                if down_fin:
                    break

            if down_fin:
                if self.fmt == 'spk':
                    if SPK(p).unpack(p[:-len(self.e_name)]):
                        self.fin_signal.emit(f)
                    else:
                        print(p, 'unpack failed.')
                elif self.fmt == 'tct':
                    if TCT(p).unpack(getdirectory(p)):
                        self.fin_signal.emit(f)
                    else:
                        print(p, 'unpack failed.')
            unlink(p)

            self.p_g_signal.emit(i, l - 1)

    def _cb_progress(self, a_size, n_size, s_time, n_time):
        self.p_s_signal.emit(n_size, a_size)
        u_time = (n_time - s_time)
        if u_time > 0:
            self.sp_signal.emit(str(n_size // u_time // 1024) + 'kb/s')

    def _cb_start(self, header):
        # print(header)
        f_size = str(int(header['Content-Length']) // 1024) + 'kb'
        self.i_signal.emit(self.f_now, f_size)
