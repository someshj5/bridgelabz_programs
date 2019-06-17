class Deque:                             # creating a class Deque
    def __init__(self):                  # Initializing the Deque as empty
        self.items = []

    def is_empty(self):                  # function to check if the deque is empty
        return self.items == []

    def addF(self, item):                # function to add from front to the Deque
        self.items.append(item)

    def addR(self, item):                # Function to add from the rear to Deque
        self.items.insert(0, item)

    def removeF(self):                  # function to remove from front in Deque
        return self.items.pop()

    def removeR(self):                  # function to remove from rear to Deque
        return self.items.pop(0)

    def size(self):                      # function to check the length of Deque
        return len(self.items)


d = Deque()                             # assigning the object to the Deque class

User = input('Enter a word to check Palindrome:')  # asks for user to enter a value

for i in User:                         # Adding the items in the value from front add
    d.addF(i)

while len(d.items) > 1:                # Checks if the length of the value is more than 1
    a = d.removeF()                    # removing the value from front
    b = d.removeR()                    # removing the value from rear
    if a == b:                         # Checks if the value removed fron both ends is same & print the value
        print(a, 'popped from front and rear')
    else:
        break
if d.is_empty() == True or d.size() == 1:  # Finally if the Deuqe is empty or 1 then the User input is PALINDROME
    print('STRING IS PALINDROME')
else:
    print('NOT A PALINDROME')
