import re                                     # importing REGULAR EXPRESSION
from datetime import date                     # importing datetime module
import sys                                    # importing sys module


def regularExp():                             # Function to replace the text using REGULAR EXPRESSION

    mystring = '''Hello <<name>>, We have your full name as <<full name>> in our system.",
                your contact number is 91-xxxxxxxxxx.",
                Please,let us know in case of any clarification 
                Thank you BridgeLabz 01/01/2016. '''

    today = date.today()
    d = today.strftime('%d/%m/%Y')
    try:
        first_name = input('Enter your firstname: ')       # asks user for input firstname
        if not re.match("^[a-zA-Z]*$", first_name):        # regex if invalid data
            print("Error! Only letters a-z allowed!")

        last_name = input('Enter your lastname')          # asks user for lastname
        if not re.match("^[a-zA-Z]*$", last_name):        # Checkiing the input usein regex
            print("Error! Only letters a-z allowed!")
            sys.exit()

        mobile = input('\n Enter your mobile number '+'\n ie: 91-xxxxxxxxxx')  # input mobile number
        if len(str(mobile)) > 10:
            raise ValueError
        if not re.match("^[0-9]*$", first_name):                               # regex to check number
            print("Error! Only numericals 0-9 allowed!")

        if first_name.isalpha() and last_name.isalpha() and  mobile.isdigit():
            Full_name = first_name + " " + last_name
            mobile = '91-'+ mobile
            data = [first_name, Full_name, mobile,d]
            pattern = ['<<name>>','<<full name>>','91-xxxxxxxxxx',' 01/01/2016']

            for i in range(4):
                mystring = re.sub(pattern[i],data[i],mystring)               # regular expression to replace patterns by User data
            print(mystring)
        else:
            raise ValueError
    except ValueError:                                                      # exception handling for value error
        print('Please specific value at specific place')


regularExp()

