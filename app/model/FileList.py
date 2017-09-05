from lib.Download import Download
from lib.NXList import NXList
from lib.TCList import TCList
from ..config import Config


class FileList:
    def __init__(self):
        self.data = []

    def update(self, src):
        downer = Download()
        # downer.event_connect('start', print)
        downer.event_connect('error', print)
        info = Config.source[src]
        data = downer.download(src + info['list'], conn_timeout=Config.conn_timeout)
        if data:
            if info['format'] == 'tct':
                tcl = TCList(data)
                self.data = [x['name'] for x in tcl.data]
            else:
                nxl = NXList(data)
                self.data = [x['name'] for x in nxl.data]
        else:
            self.data.clear()

    def search(self, keyword):
        l = []
        for f_name in self.data:
            if keyword in f_name:
                l.append(f_name)
        return l
