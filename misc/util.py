def f_readlines(file_name: str) -> list:
    """
    Given a file name it returns the file as a list
    """
    f = open(file_name)
    return f.readlines()


def freadintlist(file_name: str) -> list:
    return lmap(lambda x: int(x), f_readlines(file_name))


def lmap(fun, iterable):
    return list(map(fun, iterable))


def split_string(s):
    return [*s]
