import itertools


def func(s):
    return hash(s)


def compress_string(s):
    arr = []
    b = itertools.groupby(s, key=func)
    for i, iter in b:
        a = list(iter)
        arr.append(a[0])
        arr.append(len(a))
        print(tuple(arr), end=" ")
        arr.pop()
        arr.pop()


if __name__ == '__main__':
    compress_string('12254477')
