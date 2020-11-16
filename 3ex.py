import shutil
import os

shutil.unpack_archive('D:\МФТИ\Информатика\main.zip',
                      'D:\МФТИ\Информатика\main', 'zip')
arr = []
for dirpath, dirnames, filenames in os.walk('D:\МФТИ\Информатика\main'):
    for dirname in dirnames:
        for filename in filenames:
            if filename.endswith('.py') and dirname not in arr:
                arr.append(dirname)
arr.sort()

with open('D:\МФТИ\Информатика\oop.txt', 'w') as file:
    for line in range(len(arr)):
        file.write(arr[line])
        file.write('\n')
