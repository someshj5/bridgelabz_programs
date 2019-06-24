from temp2 import Stock                           # from temp2 importing Stock class
from linkedlist import *                          # importing  class Linkedlist from linkedlist file
import json

st = Stock
l = LinkedList()                                    # object to the Class Linked list
try:
    print('Enter 1 to print the inventory\nEnter 2 to quit')
    User = int(input('Enter a value: '))                    # Asks user for input
    if User == 1:
        l.display()                                         # if 1 then display linked list nodes
    if User == 2:                                           # if 2 the quit
        quit()
except ValueError:                                          # Exception handling for value error
    print('Invalid Input!')


def stockadd():                                                  # Function to add data to linked list nodes
    try:
        with open('Stockmarket.json','r') as f1:                 # loading json data in a variable
            loaded = json.load(f1)
            for i in loaded['data']:
                l.append(i)                                      # appending data to the linked list
        print(l.display())
    except FileExistsError:                                      # Exception handling for json file
        print('File Error')


stockadd()

def stockrem():
    User = input('Enter a stock name: ')
    with open('Stockmarket.json','r') as f1:
        load = json.load(f1)
        for i in load['data']:
            if i == User:
                l.remove(load['data'][i])
    l.display()


stockrem()


