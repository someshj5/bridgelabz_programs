
class Queue:  # creating the class as Queue

    def __init__(self):   # Initializing the Queue as empty queue
        self.queue = []

    def is_empty(self):   # Function to check if the Queue is empty
        return self.size() == 0

    def enqueue(self, val):  # function to enqueue a value into the Queue
        self.queue.insert(0, val)

    def dequeue(self):     # function to dequeue the value from the Queue
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):   # function to check the len of the queue
        return len(self.queue)

    def dispaly(self, val):  # function to display the value in the Queue
        print(val)



class Stack:   # creating a class Stack

    def __init__(self):  # function to initialize the stack as empty
        self.items = []

    def is_empty(self):    # function to check if the stack is empty
        return self.items == []

    def push(self, data):  # function to push a value in to the stack
        self.items.append(data)

    def pop(self):  # function to pop a value from a stack
        print(self.items.pop())

    def size(self):   # function to check the length of the stack
        len(self.items)

    def display(self, data):  # function to display the value in the Queue
        print(data)

    def peak(self):  # function to return the peak value of the sack
        if self.is_empty():
            return None
        return self.items[-1]


stack = Stack()   # Object assigning for stack1
stack2 = Stack()  # Object assigning for stack2
q2 = Queue()      # Object assigning for Queue

# Object assignment for Week day
a = ['SUN', 1, 8, 15, 22, 29]
b = ['MON', 2, 9, 16, 23, 30]
c = ['TUE', 3, 10, 17, 24, 31]
d = ['WED', 4, 11, 18, 25, ' ']
e = ['THU', 5, 12, 19, 26, ' ']
f = ['FRI', 6, 13, 20, 27, ' ']
g = ['SAT', 7, 14, 21, 28, ' ']

# Enqueue the Weekd day objects into the Queue
q2.enqueue(a)
q2.enqueue(b)
q2.enqueue(c)
q2.enqueue(d)
q2.enqueue(e)
q2.enqueue(f)
q2.enqueue(g)

# Deque the objects and pushing into the stack1
q2.dequeue()
stack.push(a)
q2.dequeue()
stack.push(b)
q2.dequeue()
stack.push(c)
q2.dequeue()
stack.push(d)
q2.dequeue()
stack.push(e)
q2.dequeue()
stack.push(f)
q2.dequeue()
stack.push(g)

# -------------PUSHING THE POPPED OBJECT FROM STACK TO STACK2 --------------------------------
print('\n********popped objects of stack1************************\n')
stack.pop()
stack2.push(g)
stack.pop()
stack2.push(f)
stack.pop()
stack2.push(e)
stack.pop()
stack2.push(d)
stack.pop()
stack2.push(c)
stack.pop()
stack2.push(b)
stack.pop()
stack2.push(a)

# ----------------------POPPING THE STACK2 OBJECTS ----------------------------------
print('\n************STACK2 OBJECTS************************\n')
stack2.pop()
stack2.pop()
stack2.pop()
stack2.pop()
stack2.pop()
stack2.pop()
stack2.pop()





