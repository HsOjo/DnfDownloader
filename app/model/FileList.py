class FileList:
    def __init__(self):
        self.data = []

    def update(self, src):
        self.data = ['1','2','3']

    def search(self, keyword):
        l = []
        for f_name in self.data:
            if keyword in f_name:
                l.append(f_name)
        return l
