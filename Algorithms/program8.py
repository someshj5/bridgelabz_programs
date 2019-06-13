import Util                                 # importing Util module

num = int(input('Enter the number of elements:'))      #Asks for num input of integers
ArrayofNum = []
for i in range(num):
    num2 = int(input('Enter the number:')) 
    ArrayofNum.append(num2)                    # Assigning the num as array or list
arr = ArrayofNum
Util.Utilities.bubble_sort(arr)             # calls  the staticmethod from the Utilities class for bubble sort of integers

