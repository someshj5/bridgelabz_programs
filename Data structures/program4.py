class Queue:                         # creating the class as Queue

    def __init__(self):            # Initializing the Queue as empty queue
        self.queue = []

    def is_empty(self):            # Function to check if the Queue is empty
        return self.size() == 0

    def enqueue(self, val):        # function to enqueue a value into the Queue
        self.queue.insert(0, val)

    def deque(self):            # function to dequeue the value from the Queue
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):                 # function to check the len of the queue
        return len(self.queue)

q =Queue()

# -----------------------***** SIMULATE BANKING CASH COUNTER *****------------------------------
cash = 1000                        # assigning a minimum bank cash balance
dep = 0
wid = 0
print('Enter 1 to deposit the cash')
print('Enter 2 to withdraw the cash')
print('Enter 3 to exit')

while True:
    UserChoice = int(input('Please enter a value: '))      # ask user to enter a value 1,2,3
    if UserChoice == 1:
        q.enqueue(1)                                      # enqueue the user into the cash counter queue
        Amount = int(input('Enter the amount you want to deposit: ')) # ask the amount to deposit
        if Amount == 0:
            print('Enter some amount!')
        else:
            dep += Amount
            cash += Amount
            print('Thank you cash deposited sucessfully!')
        q.deque()                                         # dequeue the user

    elif UserChoice == 2:                     # if the User choice is 2 then enqueue the user to withdrawal the eamount
        wid += 1
        q.enqueue(1)                          # Enqueue the user in the cash counter queue
        Amount = int(input('Enter the amount you want to withdraw: '))  # asks for the amount to withdrawal
        if dep >= Amount:
            dep -= Amount
            cash-= Amount
            print('Amount withdrawal sucessfully')
        else:
            print('Sorry dont have enough cash')
        q.deque()                                  # dequeue the user from the cash counter queue
    else:
        quit()                                       # quit from the cash counter Queue


