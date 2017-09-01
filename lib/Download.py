from contextlib import closing
from time import time

from requests import head, get

from lib.HsIO import HsIO


class Download:
    def __init__(self):
        self.e_func = {
            'start': [],
            'progress': [],
            'error': [],
        }
        self.c_size = 1024

    def event_connect(self, event, func):
        self.e_func[event].append(func)

    def download(self, url, path=None):
        try:
            h = head(url).headers
            for func in self.e_func['start']:
                func(h)

            l = int(h['Content-Length'])
            with closing(get(url, stream=True)) as resp:
                if path is None:
                    f = HsIO()
                else:
                    f = open(path, 'bw')
                s_time = time()
                for pdata in resp.iter_content(chunk_size=self.c_size):
                    f.write(pdata)
                    n_time = time()
                    for func in self.e_func['progress']:
                        func(l, f.tell(), s_time, n_time)
            if path is None:
                data = f.read_range(0)
                f.close()
                return data
            else:
                f.close()
                return True
        except Exception as e:
            for func in self.e_func['error']:
                func(e)
            return False


if __name__ == '__main__':
    md = Download()
    md.event_connect('progress', print)
    print(md.download('http://download.dfoneople.com/Patch/package.lst', 'package_o.lst'))
