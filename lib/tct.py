from zipfile import PyZipFile


class tct:
    def __init__(self, path):
        self.path = path

    def unpack(self, path):
        try:
            self.zip = PyZipFile(self.path)
            self.zip.extractall(path)
            return True
        except Exception as e:
            print(self.path, e)
            return False
