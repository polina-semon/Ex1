def get_cartesian_product(a,b):
    from itertools import product
    return list(map(tuple, product(a, b)))


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*get_cartesian_product(a, b))