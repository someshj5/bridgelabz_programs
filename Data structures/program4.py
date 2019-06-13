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


cash = 1000
dep = 0
wid = 0
print('Enter 1 to deposit the cash')
print('Enter 2 to withdraw the cash')
print('Enter 3 to exit')

while True:
    UserChoice = int(input('Please enter a value: '))
    if UserChoice == 1:

        q.enqueue(1)
        Amount = int(input('Enter the amount you want to deposit: '))
        if Amount == 0:
            print('Enter some amount!')
        else:
            dep += Amount
            cash += Amount
            print('Thank you cash deposited sucessfully!')
        q.dequeue()

    elif UserChoice == 2:
        wid += 1
        q.enqueue(1)
        Amount = int(input('Enter the amount you want to withdraw: '))
        if dep >= Amount:
            dep -= Amount
            cash-= Amount
            print('Amount withdrawal sucessfully')
        else:
            print('Sorry dont have enough cash')
        q.dequeue()
    else:
        quit()


