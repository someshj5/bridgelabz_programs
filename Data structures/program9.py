class Queue:   # creating the class as Queue

    def __init__(self):  # Initializing the Queue as empty queue
        self.queue = []

    def is_empty(self):  # Function to check if the Queue is empty
        return self.size() == 0

    def enqueue(self, val):  # function to enqueue a value into the Queue
        self.queue.insert(0, val)

    def deque(self):  # function to dequeue the value from the Queue
        if self.is_empty():
            return None
        else:
            print(self.queue.pop())

    def size(self):   # function to check the len of the queue
        return len(self.queue)

    def dispaly(self, val):   # function to display the value in the Queue
        print(val)


q = Queue()

#  Assigning the values to the week day object
wee = ['SUN', 'MON', 'TUE', 'WED', 'THUR', 'FRI', 'SAT']
a = ['SUN', 1, 8, 15, 22, 29]
b = ['MON', 2, 9, 16, 23, 30]
c = ['TUE', 3, 10, 17, 24, 31]
d = ['WED', 4, 11, 18, 25, ' ']
e = ['THU', 5, 12, 19, 26, ' ']
f = ['FRI', 6, 13, 20, 27, ' ']
g = ['SAT', 7, 14, 21, 28, ' ']

# Enqueue ht week day day objects
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
print('\t calender 2019')
# Deque the Week days objects
q.deque()
q.deque()
q.deque()
q.deque()
q.deque()
q.deque()
q.deque()


