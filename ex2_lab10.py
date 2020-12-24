# Пыталась считать время, но по времени ничего практически не меняется
# иногда код работает быстрее, иногда медленнее

import os
import re
import time
import threading


def thread_job(i):
    ip = "192.168.178." + str(i)
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
    print("I'm" + str(i) + "thread")
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])



start = time.time()
received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

threads = [threading.Thread(target=thread_job(i)) for i in range(20, 30)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
end = time.time()
t = end - start
print(t)
