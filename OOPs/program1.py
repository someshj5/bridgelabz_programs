import json
from temp2 import *

i = Stock()
# i.Create()
i.Open()
# i.total()
try:
    print('Enter 1 to print the Inventory\nEnter 2 to add items\nEnter 3 to quit')
    ch = int(input('Enter the value'))
    if ch == 1:
        i.printi()
    if ch ==2:
        i.addinvt()
    if ch == 3:
        i.total()
    if ch ==4:
        quit()
except FileExistsError:
    print('Inventory management fails')














#
# def inventory():
#     try:
#         with open('Inventory_management.json', 'r') as f1:
#             mydata = json.load(f1)
#             df = DataFrame
#             print(df(mydata))
#         print('\n*************************************************************\n')
#
#         print('Name','\t|\t','Price * Weight')
#         print('----------------------------')
#         for i in range(3):
#             a = mydata["Inventory"][i]["Name"]
#             b = mydata["Inventory"][i]["price"] * mydata["Inventory"][i]["weight"]
#
#             print(f"{a}\t|\t {b}\t$")
#     except IOError:
#         print('File not present')
#
# inventory()