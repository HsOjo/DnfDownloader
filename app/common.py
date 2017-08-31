def list_reduce(a: list, b: list):
    c = list(a)
    for i in b:
        if i in c:
            c.remove(i)
    return c
