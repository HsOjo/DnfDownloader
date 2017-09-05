from zipfile import ZipFile


class TCT:
    def __init__(self, path):
        self.path = path

    def unpack(self, path):
        try:
            with ZipFile(self.path) as f:
                f.extractall(path)
            return True
        except Exception as e:
            print(self.path, e)
            return False
