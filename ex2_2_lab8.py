import itertools


def get_permutations(a, n):
    b = itertools.permutations(a, n)
    b = list(b)
    b.sort()
    return b


if __name__ == '__main__':
    s = input()
    n = int(input())
    v = get_permutations(s, n)
    for i in v:
        for j in range(n):
            print(i[j], end = "")
        print(" ", end = "")
