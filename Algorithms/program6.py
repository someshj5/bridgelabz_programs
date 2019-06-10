import Util                                    # importing Util module

with open('/home/admin9/file3.txt','r') as f1: # opening the file in read mode
    lst= f1.read().split()                     # spliting the words

    word = input('Enter a word to search:')    #Ask for the word to search
    list = lst
    res  = Util.Utilities.searchword(list,word) # calling the staticmethod from the Utilities class and storing the result in variable
    if res == True:
        print('Present')
    else:
        print('Absent')
print(lst)



