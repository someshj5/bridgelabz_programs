# import numpy as np
# from numpy import *


class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, val):
        self.queue.insert(0, val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            print(self.queue.pop())

    def size(self):
        return len(self.queue)

    def dispaly(self, val):
        print(val)


q = Queue()

a = ['SUN', 1, 8, 15, 22, 29]
b = ['MON', 2, 9, 16, 23, 30]
c = ['TUE', 3, 10, 17, 24, 31]
d = ['WED', 4, 11, 18, 25, ' ']
e = ['THU', 5, 12, 19, 26, ' ']
f = ['FRI', 6, 13, 20, 27, ' ']
g = ['SAT', 7, 14, 21, 28, ' ']

q.enqueue(a)
q.enqueue(b)
q.enqueue(c)
q.enqueue(d)
q.enqueue(e)
q.enqueue(f)
q.enqueue(g)

# q.dispaly(a)
# q.dispaly(b)
# q.dispaly(c)
# q.dispaly(d)
# q.dispaly(e)
# q.dispaly(f)
# q.dispaly(g)

q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()


