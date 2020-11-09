#центр масс 3-х точек

class Vector():

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y, self.z / other.z)


n = int(input())
arr = []
С = Vector(n, n, n)
ax, ay, az = map(int, input().split())
A = Vector(ax, ay, az)
while n - 1 != 0:
    bx, by, bz = map(int, input().split())
    B = Vector(bx, by, bz)
    A = A + B
    n -= 1
V = A / С
print(V.x, V.y, V.z)