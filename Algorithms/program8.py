import Util                                 # importing Util module

num = int(input('Enter the numbers:'))      #Asks for num input of integers
ArrayofNum = list(num)                      # Assigning the num as array or list
arr = ArrayofNum
Util.Utilities.bubble_sort(arr)             # calls  the staticmethod from the Utilities class for bubble sort of integers

