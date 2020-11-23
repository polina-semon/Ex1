def swap(func_to_decorate):
    def wrapper(x, y, show):
        x, y = y, x
        if show:
            show = False
        else:
            show = True
        res = x / y
        if show:
            print(res)
        return res
    return wrapper


@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res


print(div(2, 4, show=True))