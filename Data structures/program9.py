import numpy as np


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
            return self.queue.pop()

    def size(self):
        return len(self.queue)

q =Queue()

week=['SUN', 'MON', 'TUE', 'WED', 'THUR', 'FRI', 'SAT']
day = [1, 2, 3, 4, 5, 6 ,7,
       8 , 9, 10, 11, 12, 13, 14,
       15, 16, 17, 18, 19, 20, 21,
       22, 23, 24, 25, 26, 27, 28,
       29, 30, 31]

np.
# # day = np.arange(31)
# print(np.arange(31))

# for i in range(len(week)):
#     for j in range(0,31):
#         print(day)
