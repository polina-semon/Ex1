with open("D:\МФТИ\Информатика\op.txt", "r") as file, open("D:\МФТИ\Информатика\oop.txt", "w") as file1:
    file1.write(file.read())