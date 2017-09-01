from lib.Download import Download
from lib.NXList import NXList
from ..const import Const


class FileList:
    def __init__(self):
        self.data = []

    def update(self, src):
        downer = Download()
        downer.event_connect('start', print)
        downer.event_connect('error', print)
        data = downer.download(src + Const.list_name)
        if data:
            nxl = NXList(data)
            self.data = nxl.l_file
        else:
            self.data.clear()

    def search(self, keyword):
        l = []
        for f_name in self.data:
            if keyword in f_name:
                l.append(f_name)
        return l
