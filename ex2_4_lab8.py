import itertools


def get_combinations_with_replacement(a, n):
    b = itertools.combinations_with_replacement(a, n)
    b = list(b)
    b.sort()
    return b


if __name__ == '__main__':
    s = input()
    n = int(input())
    v = get_combinations_with_replacement(s, n)
    for i in v:
        for j in range(n):
            print(i[j], end = "")
        print(" ", end = "")