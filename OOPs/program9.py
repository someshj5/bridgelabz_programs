import itertools
import random
# class Deckofcards:


rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
deck = list(itertools.product(rank, suits))


def distributed():
    for players in range(1, 5):
        random.shuffle(deck)
        print('\n')
        print('Player',players,'got 9 cards\n')
        for i in range(1,10):
            print(deck[i][0], 'of',deck[i][1])
    # deck.pop()


# deck = Deckofcards()
distributed()
#