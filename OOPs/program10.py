from program10Q import Queue                           # importing Queue from program 10q
import random                                          # importing random module
import itertools                                       # importing itertools

rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
deck = list(itertools.product(rank, suits))
# print(sorted(deck))


def distributed():                                      # Function to randomly distribute the cards to 4 players

    for players in range(1, 5):

        random.shuffle(deck)                            # random shuffle to deck cards
        print('\n')
        print('Player',players,'got 9 cards\n')
        for i in range(1,10):
            print(deck[i][0], 'of',deck[i][1])


distributed()

print('------------------------------------- DEQUE OPERATION------------------------------------------')

q = Queue()                                         # assigning object to Queue class

q.enqueue(rank)                                    # Enqueuing the rank in the Queue
q.enqueue(deck)                                    # Enqueuing deck in the Queue
# q.enqueue()                             # Enqueuing distributed cards to the Queue
print('-----------------------------------------------------------------------------')
q.dequeue()
q.dequeue()
q.dequeue()
