from address import Address
import json
import sys

try:
    a1 = Address()
    a1.Open()
    choice = int(input('Enter 1 to Add new contact\nEnter 2 to delete\nEnter 3 to Update address book\n'
                       'Enter 4 to print Address book\nEnter 5 to Quit\n: '))
    if choice ==1 :
        a1.add()
    elif choice == 2:
        a1.delete()
    elif choice == 3:
        a1.update()
    elif choice == 4:
        a1.print()
    elif choice == 5:
        sys.exit()
except FileExistsError:
    print('Error')


