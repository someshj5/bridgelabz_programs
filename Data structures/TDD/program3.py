class Stack:                          # creating a class Stack

    def __init__(self):               # function to initialize the stack as empty
        self.items = []

    def is_empty(self):               # function to check if the stack is empty
        return self.items == []

    def push(self, data):             # function to push a value in to the stack
        self.items.append(data)

    def pop(self):                    # function to pop a value from a stack
        return self.items.pop()

    def size(self):                    # function for the length of a stack
        len(self.items)

    def peak(self):                    # function for the peak value in the stack
        if self.is_empty():
            return None
        return self.items[-1]


stack = Stack()                        # assigning the stack as object

mydata = '(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)'  # expression to check for balanced parentheses


def balanced(mydata):
    for i in mydata:                         # iterate through the expression in mydata
        if i == '(':
            stack.push('(')                  # push a value in stack
        elif i == ')':
            stack.pop()                      # pop the value from the stack

    if stack.is_empty():                    # check if the stack is empty and print the result
        print ('the Expresseion has balanced parentheses')
    else:
        print('The expression is not balanced')


balanced(mydata)