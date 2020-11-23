def decorator(func_to_decorate):
    def wrapper():
        b = func_to_decorate(a)
        if len(b) == 0:
            return "Нет"
        elif len(b) > 10:
            return "Очень много"
        else:
            return b
    return wrapper


def chet_func(a):
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
    return b


a = list(map(int, input().split()))
# b = chet_func(a)
# print(*b)
func_decorated = decorator(chet_func)
print(func_decorated())