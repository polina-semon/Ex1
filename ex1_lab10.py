# "Проблемность" кода заключается в том, что если дать функции "thread_job" заснуть
# даже на очень малое время, то код начнёт работать некорректно, ибо
# два разных потока пытаются менять одни и те же данные и из-за этого происходит
# путанница, которая и приводит к некорректному ответу
# если у нас нет задержки функции потока
# вывод: 1 2 3 4 5 6 7 8 9 10 10
# если есть задержка функции потока
# вывод: 1 2 3 4 5 6 3 6 5 5 5 (1 2 3 3 2 3 2 2 2 2 2) или любой другой,
# ибо это непредсказуемо
# 1) и 2) - строки кода, которые помогают решить данную проблему

import threading
import random  # проблема
import time  # проблема
import sys


def thread_job():
    # with lock: # +tab ниже 2)
    # lock.acquire()  # mutex 1)
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1)) # проблема
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()
    # lock.release() # 1)


# lock = threading.Lock() # 1) 2)
counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)