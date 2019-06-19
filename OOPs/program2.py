import re
from datetime import date
import sys


def regularExp():

    mystring = '''Hello <<name>>, We have your full name as <<full name>> in our system.",
                your contact number is 91-xxxxxxxxxx.",
                Please,let us know in case of any clarification 
                Thank you BridgeLabz 01/01/2016. '''

    today = date.today()
    d = today.strftime('%d/%m/%Y')
    try:
        first_name = input('Enter your firstname: ')
        if not re.match("^[a-zA-Z]*$", first_name):
            print("Error! Only letters a-z allowed!")

        last_name = input('Enter your lastname')
        if not re.match("^[a-zA-Z]*$", first_name):
            print("Error! Only letters a-z allowed!")
            sys.exit()

        mobile = input('\n Enter your mobile number '+'\n ie: 91-xxxxxxxxxx')
        if len(str(mobile)) > 10:
            raise ValueError

        if not re.match("^[0-9]*$", first_name):
            print("Error! Only numericals 0-9 allowed!")

        if first_name.isalpha() and last_name.isalpha() and  mobile.isdigit():
            Full_name = first_name + " " + last_name
            mobile = '91-'+ mobile
            data = [first_name, Full_name, mobile,d]
            pattern = ['<<name>>','<<full name>>','91-xxxxxxxxxx',' 01/01/2016']

            for i in range(4):
                mystring = re.sub(pattern[i],data[i],mystring)
            print(mystring)
        else:
            raise ValueError
    except ValueError:
        print('Please specific value at specific place')


regularExp()


    # month = int(input('Enter the month in numbers: '))
    # if len(str(month)) > 2:
    #     print('Enter 2 digits only')
    # year = int(input('Enter the year: '))
    # if len(str(year)) <= 3 and len(str(year)) > 4:
    #     print('Enter 4 digits only')

    # if not re.match("^[a-z]*$", first_name):
    #     print("Error! Only letters a-z allowed!")

    # if not re.match("^[a-z]*$", Full_name):
    #     print("Error! Only letters a-z allowed!")