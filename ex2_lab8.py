def fib(n):
    a = b = 1
    _current = a
    for i in range(n):
        _next = _current + b
        b = _current
        _current = _next
        yield _next


n = int(input())
print(1, 1, *list(fib(n)))