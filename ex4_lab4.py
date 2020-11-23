import time

def decorator(main_function):
    def wrapper_of_the_function(args, way):
        start = time.time()
        main_function(args)
        end = time.time()
        t = end - start
        a = []
        a.append(start)
        a.append(args)
        a.append(end)
        a.append(t)
        if t == 0:
            a = []
            ar = '-'
            a.append(ar)
        else:
            a[2] = args
        print(a)
        with open("'", way, "'", "w") as output:
            output.write(a)
        return
    return wrapper_of_the_function

@decorator
def main_function(args):
    # функция