from io import BytesIO, FileIO, IOBase
from struct import unpack, calcsize


class HsIO(IOBase):
    def __init__(self, path=None, mode='r'):
        super().__init__()
        self.io = None
        if type(path) == str:
            self.io = FileIO(path, 'b' + mode)
        else:
            self.io = BytesIO(path)
        HsIO.__overwrite__(self.io, self)

    @staticmethod
    def __overwrite__(core, ins):
        ins.read = core.read
        ins.write = core.write
        ins.seek = core.seek
        ins.tell = core.tell
        ins.close = core.close
        ins.readline = core.readline
        ins.fileno = core.fileno
        ins.flush = core.flush
        ins.isatty = core.isatty
        ins.readable = core.readable
        ins.readlines = core.readlines
        ins.seekable = core.seekable
        ins.truncate = core.truncate
        ins.writable = core.writable
        ins.writelines = core.writelines

    def peek(self, *args, **kwargs):
        p = self.tell()
        data = self.read(*args, **kwargs)
        self.seek(p)
        return data

    def read(self, *args, **kwargs):
        pass

    def write(self, *args, **kwargs):
        pass

    def read_string(self, maxsize=-1, to_ms=False):
        tgt = 0
        if to_ms:
            tgt = self.tell() + maxsize

        ret = ''
        while len(ret) < maxsize or maxsize == -1:
            data = self.read(1)
            if len(data) != 1:
                break
            [tmp] = unpack('B', data)
            if tmp != 0:
                ret += chr(tmp)
            else:
                break

        if to_ms:
            self.seek(tgt)
        return ret

    def read_param(self, mask, fix=True):
        size = calcsize(mask)
        data = self.read(size)
        if fix:
            for i in range(size - len(data)):
                data += b'\x00'
        return unpack(mask, data)

    def read_range(self, offset, size=-1):
        self.seek(offset)
        return self.read(size)
