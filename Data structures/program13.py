from program12 import anagrams    # importing anagrams array from program12


class Stack:  # creating a class Stack

    def __init__(self):  # function to initialize the stack as empty
        self.items = []

    def is_empty(self):  # function to check if the stack is empty
        return self.items == []

    def push(self, data):  # function to push a value in to the stack
        self.items.append(data)

    def pop(self):  # function to pop a value from a stack
        print(self.items.pop())

    def size(self):   # function for the length of a stack
        len(self.items)

    def peak(self):   # function for the peak value in the stack
        if self.is_empty():
            return None
        return self.items[-1]


stack = Stack()    # Object assigning for stack


for a in anagrams:  # iterating through the items in anagram array
    stack.push(a)   # pushing the items in stack
print('****************')
for i in anagrams:
    stack.pop()       # pop the items from the stack
