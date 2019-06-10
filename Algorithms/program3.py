import Util
from program2 import * #importing Prime numbers array from Program 2

#----------------Palindrome of Prime Numbers-------------------------


print('Palindrome Number of prime numbers are:')
N1 = primeArr #Assigning N1 as variable for prime numbers Array
Util.Utilities.Palindrome_num(N1) #Calls the staticmethod from the  Utilities Class for Palindrome of prime numbers


#-----------Anagram of Prime Numbers-------------------------------
print
print('---------------------------------------------')
print('Anagram of prime number are:')
primearr = primeArr #Assigning the variable
Util.Utilities.Prime_anagram(primearr) #calls the staticmethod from the Utilties class for Anagram of Prime numbers
