import json
import sys


class Address:

    def __init__(self):
        self.lst = {}
        self.filename = None

    def Create(self):
        self.lst = {'data':[]}
        filename = input('Enter a file name')
        with open(filename+'.json','w') as f1:
            json.dump(self.lst,f1,indent=2)
            f1.close()
            print(filename, 'File created')

    def Open(self):
        filename = input('Enter the file name')
        with open(filename+'.json','r') as f1:
            self.lst = json.load(f1)


    def sort(self):
        print(self.lst)
        self.lst = sorted(self.lst)
        print(self.lst)

    def add(self):
        addnew={}
        try:
            first_name = input('Enter your first name: ')
            last_name = input('Enter your lastname: ')
            mobile = input('Enter the mobile number: ')
            address= input('Enter the address: ')
            zipcode = input('Enter your pincode: ')
            city = input('Enter your city name: ')
            state = input('Enter your state name: ')
            if (first_name.isalpha() and last_name.isalpha() and mobile.isnumeric()and
            address.isalpha()and zipcode.isnumeric()and city.isalpha()and state.isalpha()):
                addnew['firstname'] = first_name
                addnew['lastname'] = last_name
                addnew['mobile'] = mobile
                addnew['address'] = address
                addnew['zipcode'] = zipcode
                addnew['city'] = city
                addnew['state'] = state
                self.lst['data'].append(addnew)
                self.save()
                self.print()
        except ValueError:
            print('You entered wrong data!')
            self.add()
            return

    def update(self):
        try:
            flag = update = False
            if len(self.lst['data']) >= 1:
                first_name = input('Enter the firstname: ')
                last_name = input('Enter  the lastname: ')
                for i in range(len(self.lst['data'])):
                    if (str(self.lst['data'][i]['firstname']).casefold() == first_name.casefold()
                            and str(self.lst['data'][i]['lastname']).casefold() == last_name.casefold()):
                        print('ttt')
                        flag = True
                    if flag == True:
                        print('Enter 1 to update city')
                        print('Enter 2 to update Address')
                        print('Enter 3 to update State')
                        print('Enter 4 to update mobile')
                        print('Enter 5 to update zipcode')
                        user = int(input('Enter your choice: '))
                        if user ==1:
                            city = input('Enter New City name: ')
                            self.lst['data'][i]['city'] = city
                            update = True
                        elif user == 2:
                            address = input('Enter New address: ')
                            self.lst['data'][i]['address'] = address
                            update = True
                        elif user == 3:
                            state = input('Enter New state name: ')
                            self.lst['data'][i]['state'] =state
                            update = True
                        elif user == 4:
                            mobile = input('Enter New mobile number: ')
                            self.lst['data'][i]['mobile'] = mobile
                            update = True
                        elif user == 5:
                            zipcode = input('Enter the new zipcode:')
                            self.lst['data'][i]['zipcode'] = zipcode
                            update = True
                        else:
                            print('Invalid input')
                            update = False
                            self.print()
                    else:
                        print('Enter numericals only')
                        self.update()
            else:
                print('Enter valid name:')
                self.update()
        except:
            print('Invalid input')
        if update:
            self.save()
            self.print()

    def save(self):
        filename = input('Enter the file name: ')
        with open(filename+'.json','w') as j1:
            json.dump(self.lst, j1, indent=2)
            j1.close()

    def print(self):
        try:
            if len(self.lst['data']) >= 1:
                print('\n------------- ADDRESS BOOK ---------------\n')
                print('First Name\t\tLast Name\t  Mobile number\t  Address\t City\t\tState\t\t\tZipcode')
                print('-----------------------------------------------------------------------------------------------')
                for i in range(len(self.lst['data'])):
                    print(self.lst['data'][i]['firstname'],'\t  ',self.lst['data'][i]['lastname'],
                          self.lst['data'][i]['mobile'],'\t\t',self.lst['data'][i]['address'],'\t',
                          self.lst['data'][i]['city'],'\t',self.lst['data'][i]['state'],'\t',
                          self.lst['data'][i]['zipcode'])
            else:
                print('No record found')
                ch = input('Do you want to Add new record? : Enter = y/n ')
                if ch.upper == Y:
                    self.add()
                else:
                    sys.exit()
        except:
            print('File is empty')

    def delete(self):
        first_name = input('Enter the firstname: ')
        last_name = input('Enter  the lastname: ')
        for i in range(len(self.lst['data'])):
            if (str(self.lst['data'][i]['firstname']).casefold() == first_name.casefold()
                    and str(self.lst['data'][i]['lastname']).casefold() == last_name.casefold()):
                print('deleted succesfully')
                del self.lst['data'][i]
                self.save()
                self.print()
                return
            else:
                print('No data found')






