import json

def inventory():
    try:
        with open('Inventory_management.json', 'r') as f1:
            mydata = json.load(f1)

        print('Name', '\t', 'Value')

        for i in range(3):
            a = mydata["Inventory"][i]["Name"]
            b = mydata["Inventory"][i]["price"] * mydata["Inventory"][i]["weight"]

            print(f"{a} \t {b}")
    except IOError:
        print('File not present')

inventory()