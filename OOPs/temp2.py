import json                                           # importing json module


class Stock:                                          # class Stock created

    def __init__(self):
        self.lst = {}

    def Create(self):                                 # method to create a json file
        self.lst = {'data':[]}
        filename = input('Enter file name: ')
        with open(filename+'.json', 'w') as f1:
            json.dump(self.lst, f1, indent=2)
            f1.close()

    def Open(self):                                    # method to open a json file
        filename = input('Enter the filename: ')
        with open(filename+'.json', 'r') as f1:
            self.lst= json.load(f1)
            print('file opened successfully!')

    def addst(self):                                   # method to add stock data to the file
        addnew = {}
        try:
            stockname = input('Enter the stockaname: ')
            stockprice = int(input('Enter the price per stock: '))
            shares = int(input('Enter the shares you want: '))
            addnew['stockname'] = stockname
            addnew['stockprice'] = stockprice
            addnew['shares'] = shares
            self.lst['data'].append(addnew)
            self.save()
            self.print()
        except ValueError:
            print('You entered Wrong data!')
            self.addst()
            return

    def delete(self):                                  # method to delete json data from the file
        stockname = input('Enter the name of the stock: ')
        for i in range(len(self.lst['data'])):
            if str(self.lst['data'][i]['stockname']).casefold() == stockname.casefold():
                del self.lst['data'][i]
                self.save()
                self.print()

    def print(self):                                     # method to print the json data
        if len(self.lst['data']) >= 1:
            print('-------------------Inventory Management-------------------')
            print('Stockname\t\tStockprice\t\tShares')
            print('-----------------------------------------------------------')
            for i in range(len(self.lst['data'])):
                print(self.lst['data'][i]['stockname'],'\t\t\t',self.lst['data'][i]['stockprice'],'\t\t\t',
                      self.lst['data'][i]['shares'])
        else:
            print('No record found')
            ch = input('Do you want to add new stockvalue: Y/N')
            if ch.upper() == 'Y':
                self.addst()
            else:
                quit()

    def save(self):                                      # method to save the data to the json file
        filename = input('Enter the file name')
        with open(filename+'.json', 'w') as f1:
            json.dump(self.lst, f1, indent=2)
            f1.close()

# ---------------------------------*** INVENTORY MANGEMENT ***--------------------------------------------
    def addinvt(self):                                      # method to add inventory items to file
        addn = {}
        try:
            itemname = input('Enter the name of item: ')
            weight = int(input('Enter the weight: '))
            price = int(input('Enter the price: '))
            if itemname.isalpha():
                addn['Name'] = itemname
                addn['weight'] = weight
                addn['price'] = price
                self.lst['data'].append(addn)
                self.save()
                self.printi()
        except ValueError:
            print('Enter valid details!')

    # def total(self):                                              # method to calculate the total amount
    #     addn = {}
    #     for i in range(len(self.lst['data'])):
    #         totalp = self.lst['data'][i]['price'] * self.lst['data'][i]['weight']
    #         addn["Total"]=totalp
    #         self.lst['data'].append(addn)
    #         self.save()
    #         self.printi()

    def printi(self):                                              # method to print the Inventory file
        addn = {}
        if len(self.lst['data']) >= 1:
            print('-------------- INVENTORY------------------------')
            print('Item\t\tWeight\t\tPrice')
            print('------------------------------------------------')
            for i in range(len(self.lst['data'])):
                print(self.lst['data'][i]['Name'],'\t\t',self.lst['data'][i]['weight'],'\t\t',
                      self.lst['data'][i]['price'])
        else:
            print('No items in Inventory')
            ch = input('Do you want to add items: Y/N')
            if ch.upper() == 'Y':
                self.addinvt()
            else:
                quit()




