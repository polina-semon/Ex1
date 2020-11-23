# если сильно менять N (в 5 - 10 раза) в теле программы, то можно увидеть,
# что время её выполнения с увеличением N будет увеличиваться
# N = 50   t = 0,012 0,015 0,012 0,031
# N = 100  t = 0,031 0,047 0,031 0,031
# N = 500  t = 0,187 0,187 0,171 0,196
# N = 1000 t = 0,438 0,360 0,372 0,343

import threading
import time
import random


def thread_job(i):
    global counter
    counter += i


if __name__ == '__main__':
    counter = 0
    start = time.time()
    N = 1000
    arr = []
    while N != 0:
        a = random.randint(-10, 10)
        arr.append(a)
        N -= 1
    print(*arr)
    threads = [threading.Thread(target=thread_job(arr[i])) for i in range(len(arr))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    t = end - start
    print(counter)
    print(t)
