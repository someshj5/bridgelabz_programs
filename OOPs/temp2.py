import json


class Stock:

    def __init__(self):
        self.lst = {}

    def Create(self):
        self.lst = {'data':[]}
        filename = input('Enter file name: ')
        with open(filename+'.json', 'w') as f1:
            json.dump(self.lst, f1, indent=2)
            f1.close()

    def Open(self):
        filename = input('Enter the filename: ')
        with open(filename+'.json', 'r') as f1:
            self.lst= json.load(f1)
            print('file opened successfully!')

    def addst(self):
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

    def delete(self):
        stockname = input('Enter the name of the stock: ')
        for i in range(len(self.lst['data'])):
            if str(self.lst['data'][i]['stockname']).casefold() == stockname.casefold():
                del self.lst['data'][i]
                self.save()
                self.print()

    def print(self):
        if len(self.lst['data']) >= 1:
            print('-------------------Inventory Management-------------------')
            print('Stockname\t\tStockprice\t\tShares')#\t\tTotal')
            print('-----------------------------------------------------------')
            for i in range(len(self.lst['data'])):
                print(self.lst['data'][i]['stockname'],'\t\t\t',self.lst['data'][i]['stockprice'],'\t\t\t',
                      self.lst['data'][i]['shares'])#,self.lst['data'][i]['Total'])
        else:
            print('No record found')
            ch = input('Do you want to add new stockvalue: Y/N')
            if ch.upper() == Y:
                self.addst()
            else:
                quit()

    def save(self):
        filename = input('Enter the file name')
        with open(filename+'.json', 'w') as f1:
            json.dump(self.lst, f1, indent=2)
            f1.close()


    def addinvt(self):
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

    def total(self):
        addn = {}
        for i in range(len(self.lst['data'])):
            totalp = self.lst['data'][i]['price'] * self.lst['data'][i]['weight']
            addn["Total"]=totalp
            self.lst['data'].append(addn)
            self.save()
            self.printi()

    def printi(self):
        if len(self.lst['data']) >= 1:
            print('-------------- INVENTORY------------------------')
            print('Item\t\tWeight\t\tPrice\t\tTotal')
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




