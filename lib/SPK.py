from bz2 import decompress

from .HsIO import HsIO


class SPK:
    h_mark = b'\x11\xb1\x01\x00'

    def __init__(self, path):
        self.io = HsIO(path)
        self.path = path

        self.name = ''
        self.data = b''
        self.size = 0

        self.real = False

    def unpack(self, path=None):
        try:
            self.io.seek(0)
            h_mark = self.io.read(4)  # 11 B1 01 00
            if h_mark == SPK.h_mark:
                self.name = self.io.read_string(260, True)
                [u_mark, g_size] = self.io.read_param('<ii')  # u_mark:200
                hash = self.io.read(32).hex()

                [dc_size] = self.io.read_param('<i')  # part decompress size.
                [p_count] = self.io.read_param('<i')
                p_offset = self.io.read_param('<' + 'i' * p_count)

                tmp = HsIO(path, 'w')
                for i in range(p_count):
                    cpos = self.io.tell()

                    [p_zip, p_size] = self.io.read_param('<ii')

                    # p_mark:FE FF FF FF/FF FF FF FF
                    # r_size:-p_size-1
                    [p_mark, r_size] = self.io.read_param('<ii')

                    p_hash = self.io.read(32).hex()

                    if p_zip != 0:
                        c_data = self.io.read(p_size)
                        p_data = decompress(c_data)
                    else:
                        p_data = self.io.read(p_size)

                    self.io.seek(cpos + p_offset[i])
                    tmp.write(p_data)

                self.real = tmp.tell() == g_size
                if self.real:
                    if path is None:
                        self.data = tmp.read_range(0)
                    self.size = g_size
                    return True
                else:
                    raise Exception('Size Error:file maybe brock!')
        except Exception as e:
            print(self.path, e)
            return False


if __name__ == '__main__':
    ins = SPK('../download/Music/shallow_keep_b01.ogg')
    ins.unpack()
    print(ins.real)
    # from os import walk
    # for d, ds, fs in walk('../download'):
    #     for f in fs:
    #         i = '%s/%s' % (d, f)
    #         ins = spk(i)
    #         ins.unpack()
    #         print(i, ins.real)
