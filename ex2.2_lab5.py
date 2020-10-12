# Лаба 5 Упражнение 2.2

class Mother():

    def __str__(self):
        return 'I am mother'


class Daughter(Mother):
    def __str__(self):
        return 'I am daughter'


m = Mother()
d = Daughter()
print(m)
print(d)