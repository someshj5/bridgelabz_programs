
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

    def dispaly(self, val):
        print(val)



class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        print(self.items.pop())

    def size(self):
        len(self.items)

    def display(self, data):
        print(data)

    def peak(self):
        if self.is_empty():
            return None
        return self.items[-1]


stack = Stack()
stack2 = Stack()
q2 = Queue()

a = ['SUN', 1, 8, 15, 22, 29]
b = ['MON', 2, 9, 16, 23, 30]
c = ['TUE', 3, 10, 17, 24, 31]
d = ['WED', 4, 11, 18, 25, ' ']
e = ['THU', 5, 12, 19, 26, ' ']
f = ['FRI', 6, 13, 20, 27, ' ']
g = ['SAT', 7, 14, 21, 28, ' ']

q2.enqueue(a)
q2.enqueue(b)
q2.enqueue(c)
q2.enqueue(d)
q2.enqueue(e)
q2.enqueue(f)
q2.enqueue(g)


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





