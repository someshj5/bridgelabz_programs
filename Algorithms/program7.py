import Util                                # importing Util module

Stringg = input('Please enter few names:') #Ask for words as input
str1 = list(Stringg)                       # Assigninf the str1 as a list

Util.Utilities.sort_string(str1)           # call the the staticmethod from the Utilities class to using insertion sort for string
