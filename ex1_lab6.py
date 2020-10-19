# Лаба 6 Упражнение 1

class Complex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        v = self.a+other.a
        w = self.b+other.b
        if w < 0:
            return '(' + str(v) + str(w) + 'j' + ')'
        else:
            return '(' + str(v) + "+" + str(w) + 'j' + ')'

    def __sub__(self, other):
        v = self.a - other.a
        w = self.b - other.b
        if w < 0:
            return '(' + str(v) + str(w) + 'j' + ')'
        else:
            return '(' + str(v) + "+" + str(w) + 'j' + ')'

    def __mul__(self, other):
        v = self.a*other.a - self.b*other.b
        w = self.b*other.a + self.a*other.b
        if w < 0:
            return '(' + str(v) + str(w) + 'j' + ')'
        else:
            return '(' + str(v) + "+" + str(w) + 'j' + ')'

    def __truediv__(self, other):
        v = (self.a*other.a + self.b*other.b)/(other.a*other.a + other.b*other.b)
        w = (self.b*other.a - self.a*other.b)/(other.a*other.a + other.b*other.b)
        if w < 0:
            return '(' + str(v) + str(w) + 'j' + ')'
        else:
            return '(' + str(v) + "+" + str(w) + 'j' + ')'



a, b = map(int, input().split())
c, d = map(int, input().split())
x = Complex(a, b)
y = Complex(c, d)
z1 = x + y
z2 = x - y
z3 = y - x
z4 = x * y
z5 = x / y
z6 = y / x
print(z1, z2, z3, z4, z5, z6, sep='\n')




