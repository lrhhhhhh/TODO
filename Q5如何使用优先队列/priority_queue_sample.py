from random import randint
from queue import PriorityQueue
import heapq


class Point:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __repr__(self):
        return 'Point(%s %s %s)' % (self.x, self.y, self.cost)

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        elif self.cost == other.cost:
            if self.x < other.x:
                return True
            elif self.x == other.x:
                return self.y < other.y
        else:
            return False


def use_priority_queue():
    pq = PriorityQueue()
    for i in range(0, 11):
        pq.put(Point(randint(-10, 10), randint(-10, 10), randint(-1000, 1000)))

    while not pq.empty():
        print(pq.get())


def use_heapq():
    heap = []
    for i in range(0, 11):
        heapq.heappush(heap, Point(randint(-10, 10), randint(-10, 10), randint(-1000, 1000)))

    while heap:
        print(heapq.heappop(heap))


if __name__ == '__main__':
    use_priority_queue()

    print('-' * 30)

    use_heapq()