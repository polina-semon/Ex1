# Лаба 5 Упражнение 2.1

class Shape:

    def __init__(self, height, width):
       self.h = height
       self.w = width

    # def get_h(self):
    #     return self.h
    #
    # def get_w(self):
    #     return self.w


class Triangle(Shape):

    def area(self):
        return 0.5*self.h*self.w


class Rectangle(Shape):

    def area(self):
        return self.h*self.w


height = int(input())
width = int(input())
s = Shape(height, width)
t = Triangle(height, width)
r = Rectangle(height, width)

print(t.area())
print(r.area())


