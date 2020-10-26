def my_map(function, iterable, *rest):
    for elements in zip(iterable, *rest):
        yield function(elements)
#

def my_zip(*rest):
    n = len(rest[0])
    for i in range(n):
        a = []
        for j in rest:
            a.append(j[i])
        yield tuple(a)

if __name__ == '__main__':

    names = ["Alex", "Bob", "Alice", "John", "Ann"]
    age = [25, 17, 34, 24, 42]
    sex = ["M", "M", "F", "M", "F"]

    for values in my_zip(names, age, sex):
        # print("name: {} age: {} sex: {}".format(*values))
        print(values)


