import sys
import argparse


def fib(n):
    cur = 1
    if n > 2:
        cur = fib(n - 1) + fib(n - 2)
    return cur


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', default=1, type=int)

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    # print(namespace)
    v = fib(namespace)
    print(v)