# t = 2,45 - 3,46 без потоков
# t = 3,03 3,29 2,51

import urllib.request
import time
import threading


def thread_job(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


if __name__ == '__main__':
    start = time.time()
    urls = [
        'https://www.yandex.ru', 'https://www.google.com',
        'https://habrahabr.ru', 'https://www.python.org',
        'https://isocpp.org',
    ]
    threads = [threading.Thread(target=thread_job(urls[i])) for i in range(len(urls))]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    t = end - start
    print(t)
