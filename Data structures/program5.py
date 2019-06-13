class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def addF(self, item):
        self.items.append(item)

    def addR(self, item):
        self.items.insert(0, item)

    def removeF(self):
        return self.items.pop()

    def removeR(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

d = Deque()

User = input('Enter a word to check Palindrome:')

for i in User:
    d.addF(i)

while len(d.items) > 1:
    a = d.removeF()
    b = d.removeR()
    if a == b:
        print(a, 'popped from front and rear')
    else:
        break
if d.is_empty() == True or d.size() == 1:
    print('STRING IS PALINDROME')
else:
    print('NOT A PALINDROME')
