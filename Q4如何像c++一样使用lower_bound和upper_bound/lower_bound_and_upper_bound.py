from bisect import bisect_left, bisect_right
from random import randint


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point(%s %s)' % (self.x, self.y)

    def __le__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            return self.y <= other.y
        else:
            return False

    def __ge__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            return self.y >= other.y
        else:
            return False

    def __lt__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            return self.y < other.y
        else:
            return False

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            return self.y > other.y
        else:
            return False


if __name__ == '__main__':
    L = list()
    for i in range(1, 11):
        L.append(Point(randint(-10, 10), randint(-10, 10)))
    L.append(Point(-10, -8))
    L.append(Point(-10, -10))
    L.append(Point(10, 10))
    L.append(Point(10, 12))
    L.sort()
    print(L)
    index1 = bisect_left(L, Point(-10, -10))
    index2 = bisect_right(L, Point(10, 10))
    print(index1)
    print(index2)

    index3 = bisect_left(L, Point(-10, -9))
    index4 = bisect_right(L, Point(10, 11))
    print(index3)
    print(index4)
