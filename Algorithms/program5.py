import Util                            # importing Util module
import sys                             # importing sys module

N = int(sys.argv[1])                   #Ask for command line input
N = 2 ** N 
Arr = []
for i in range(0,N-1):
    Arr.append(i)
print(Arr)

arr = Arr                            #assingning the aprametes for call function
l = 0                                #assingning the aprametes for call function
r = len(Arr)-1                       #assingning the aprametes for call function


val = int(input('Enter a value :'))  #Ask the input value to search
res = Util.Utilities. binary_search(l, r, val, Arr) # calls the Utilities class for binary search
if res:
    print('True')
else:
    print('False')     
