import json
from pandas import DataFrame



def inventorymanagement():

    with open('Inventory_management.json','r') as file1:
        InventoryM = json.load(file1)
        # print(InventoryM["Inventory"])
        for i in range(3):
            a = InventoryM["Inventory"][i]["Name"]
            b = InventoryM["Inventory"][i]["price"]
            total = InventoryM["Inventory"][i]["price"] * InventoryM["Inventory"][i]["weight"]
            df = DataFrame(InventoryM)

            print(f'{a}\t\t{b} \t\t {total}')
    # print(df)
    print('Enter 1 to display the Inventory')
    print('Enter 2 to add items to the Inventory')
    print('Enter 3 to remove items from Inventory')
    print('Enter 4 to exit')
    while True:
        User = int(input('Enter the number for valid action: '))
        if User == 1:
            print(df)
        if User == 2:
            with open('Inventory_management.json', 'w+') as f1:
                item_name = input('Enter the name of the item')
                item_weight = input('Enter the weight in kilograms to add')
                item_price = input('Enter the amount per kg')
                # print(f'{item_name,item_price,item_weight}')
                data = {"Name":item_name,"weight":item_weight,"price":item_price}

                InventoryM.update(data)
                df1 = DataFrame(InventoryM)
                print(df1)
                json.dump(InventoryM, f1)
                # print(data)
        print(df)
        if User == 3:
            pass
        if User == 4:
            quit()


inventorymanagement()












# class Market:
#
#     def inventorymanagement(self):
#         with open('Inventory_management.json','r') as file1:
#             InventoryM = json.load(file1)
#             # print(InventoryM)
#             for i in range(3):
#                 a = InventoryM["Inventory"][i]["Name"]
#                 b = InventoryM["Inventory"][i]["price"]
#                 total = InventoryM["Inventory"][i]["price"] * InventoryM["Inventory"][i]["weight"]
#                 print(f'{a}\t\t{b} \t\t {total}')
#         return
#             # print(InventoryM["Inventory"])
#     def additems(self):
#         with open('Inventory_management.json','r') as file1:
#             InventoryM = json.load(file1)
#         with open('Inventory_management.json','a') as f1:
#             json.dump(InventoryM,f1)
#
#
#         # with open('Inventory_management.json','a') as file1:
#         #     InventoryAdd = json.dump(file)
#
# m = Market()



#
#

