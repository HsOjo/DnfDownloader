def list_reduce(a: list, b: list):
    c = list(a)
    for i in b:
        if i in c:
            c.remove(i)
    return c


def getdirectory(path: str):
    tmp = path.replace('\\', '/')
    return tmp[:tmp.rfind('/') + 1]


def getfilename(path: str):
    tmp = path.replace('\\', '/')
    return tmp[tmp.rfind('/') + 1:]
