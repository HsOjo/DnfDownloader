from .HsIO import HsIO


class NXList:
    def __init__(self, data):
        self.l_file = []
        self.l_sha = []

        with HsIO(data) as io:
            io.seek(40)

            def read_file(num, d):
                for i in range(num):
                    [l_name] = io.read_param('<i')
                    name = io.read(l_name)[:-1].decode('utf8')
                    io.read(8)
                    [l_sha] = io.read_param('<i')
                    sha = io.read(l_sha).hex()
                    if d != '':
                        self.l_file.append('%s/%s' % (d, name))
                    else:
                        self.l_file.append(name)
                    self.l_sha.append(sha)

            def read_dir():
                [_, l_name] = io.read_param('<ii')
                name = ''
                if l_name > 0:
                    name = io.read(l_name)[:-1].decode('utf8')
                [num] = io.read_param('<i')
                read_file(num, name)

            while io.tell() < len(data):
                read_dir()
