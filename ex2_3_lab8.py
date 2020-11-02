import itertools


def get_combinations(a, k):
    b = itertools.combinations(a, k)
    b = list(b)
    b.sort()
    return b


if __name__ == '__main__':
    m = []
    l = ""
    s = input()
    k = int(input())
    for y in range(1, k+1):
        v = get_combinations(s, y)
        for i in v:
            for j in range(y):
                l = str(l) + str(i[j])
            m.append(l)
            l = ""
    print(m)
