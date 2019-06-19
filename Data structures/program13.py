 # importing anagrams array from program12

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:  # creating a class Stack

    def __init__(self):  # function to initialize the stack as empty
        self.head = None

    def is_empty(self):  # function to check if the stack is empty
        return self.items == []

    def push(self, data):  # function to push a value in to the stack
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):      # function to pop a value from a stack
        if self.head is None:
            return None
        else:
            popping = self.head.data
            self.head = self.head.next
            return popping

# -----------------------------*** PRIME NUMBERS ***------------------------------------------------------------


N = 1000              # Prime numbers till 1000 asssigned in a variable
primeArr = []         # creating a empty array for prime numbers


def getprime(N,primeArr):  # Function to get the prime numbers till 1000
    for num in range(0, N + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                # print(num)
                primeArr.append(num)


getprime(N, primeArr)


# ---------------------------------------------*** ANAGRAM OF PRIME NUMBERS ***-----------------------------------------

primearr = primeArr
anagrams = []


def Prime_anagram(primearr):    # function to get anagram of prime numbers
    for i in primearr:
        primearr.remove(i)
        for j in primearr:
            i = str(i)
            j = str(j)
            if sorted(i) == sorted(j) and j not in anagrams and i not in anagrams:
                anagrams.append(i)
                anagrams.append(j)
                # print(i, 'and', j)


Prime_anagram(primearr)

stack = Stack()    # Object assigning for stack

# anagrams.sort()
print('\n Anagrams of prime numbers are ')
print(anagrams)


for a in anagrams:  # iterating through the items in anagram array
    a = int(a)
    stack.push(a)   # pushing the items in stack

print()
print('*****************************************************************************************************************************************************************')
print('\n Anagram in reversed order are:')
reverse = []
for i in anagrams:
    i = stack.pop()       # pop the items from the stack
    reverse.append(i)
reverse.sort(reverse = True)
print(reverse)
