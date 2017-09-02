from .HsIO import HsIO


class NXList:
    def __init__(self, data):
        self.data = []

        with HsIO(data) as io:
            io.seek(40)

            def read_file(num, d):
                for i in range(num):
                    [l_name] = io.read_param('<i')
                    f_name = io.read_string(l_name, True)
                    [size, u] = io.read_param('<ii')
                    [l_sha] = io.read_param('<i')
                    sha = io.read(l_sha).hex()
                    if d != '':
                        name = '%s/%s' % (d, f_name)
                    else:
                        name = f_name
                    self.data.append({'name': name, 'sha': sha, 'size': size})

            def read_dir():
                [_, l_name] = io.read_param('<ii')
                name = ''
                if l_name > 0:
                    name = io.read(l_name)[:-1].decode('utf8')
                [num] = io.read_param('<i')
                read_file(num, name)

            while io.tell() < len(data):
                read_dir()
