import itertools


def maximize(lists, m):
    arr = []
    for i in lists:
        b = max(i)
        a = itertools.starmap(pow, [(b, 2)])
        a = list(map(int, a))
        a = int(a[0])
        arr.append(a)
    ar = list(itertools.accumulate(arr))
    v = ar.pop()
    print(v % m)


if __name__ == '__main__':
    lists = [
        [5, 4],
        [7, 8, 9],
        [5, 7, 8, 9, 10]
    ]
    maximize(lists, m=1000)