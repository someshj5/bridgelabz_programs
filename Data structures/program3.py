class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()

    def size(self):
        len(self.items)

    def peak(self):
        if self.is_empty():
            return None
        self.items[-1]

stack = Stack()

mydata = '(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)'

for i in mydata:
    if i == '(':
        stack.push('(')
    elif i == ')':
        stack.pop()

if stack.is_empty():
    print ('the Expresseion has balanced parentheses')
else:
    print('The expression is not balanced')