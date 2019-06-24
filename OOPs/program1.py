import json                                    # importing josn
from temp2 import *                            # importing temp2 module

i = Stock()                                     # Assigning object to the stock class
i.Open()

try:
    print('Enter 1 to print the Inventory\nEnter 2 to add items\nEnter 3 to quit')
    ch = int(input('Enter the value'))                 # ask User for input
    if ch == 1:                                        # if 1 then print the inventory
        i.printi()
    if ch == 2:                                        # if 2 then add items to the inventory
        i.addinvt()
    if ch == 3:                                        # else quit
        quit()
except FileExistsError:                                # exception handling for file
    print('Inventory management fails')


def inventory():                                     # function to calculate the value for item
    try:
        with open('Inventory_management.json', 'r') as f1:         # opening json file in read mode
            mydata = json.load(f1)

        print('\n*************************************************************\n')

        print('Name','\t|\t','Price * Weight')
        print('----------------------------')
        for i in range(len(mydata['data'])):                     # for loop used to calculate the json price and weight
            a = mydata["data"][i]["Name"]
            b = mydata["data"][i]["price"] * mydata["data"][i]["weight"]
            print(f"{a}\t\t\t{b}\t$")

    except IOError:                                           # exception handling for json file
        print('File not present')

inventory()