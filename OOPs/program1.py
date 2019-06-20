import json
from pandas import DataFrame


def inventory():
    try:
        with open('Inventory_management.json', 'r') as f1:
            mydata = json.load(f1)
            df = DataFrame
            print(df(mydata))
        print('\n*************************************************************\n')

        print('Name','\t|\t','Price * Weight')
        print('----------------------------')
        for i in range(3):
            a = mydata["Inventory"][i]["Name"]
            b = mydata["Inventory"][i]["price"] * mydata["Inventory"][i]["weight"]

            print(f"{a}\t|\t {b}\t$")
    except IOError:
        print('File not present')

inventory()