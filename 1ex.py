# Лаба 3 Упражнение 1
# программа убирает пробелы из начала и конца каждой строчки файла и выводит результат в консоль
with open("D:\МФТИ\Информатика\op.txt", "r") as file:
    # print(file.read())
    n = -1
    k = -1
    for line in file:
        i = 0
        while line[i] == " ":
            i += 1
        n = i
        if len(line) == 2:
            i = 1
        else: i = len(line) - 2
        while line[i] == " ":
            i -= 1
        k = i
        # print(n, k)
        print(line[n:(k+1)])

# Создание файла
# with open("D:\МФТИ\Информатика\oop.txt", "w") as file:
#     for i in range(3):
#         file.write("AB+9\n")
#     file.write("ABYF+9\n")
#     file.write("AB+97  \n")