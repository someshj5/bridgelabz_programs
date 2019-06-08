import Util

with open('/home/admin9/file3.txt','r') as f1:
    lst= f1.read().split()

    word = input('Enter a word to search:')
    list = lst
    res  = Util.Utilities.searchword(list,word)
    if res == True:
        print('Present')
    else:
        print('Absent')
print(lst)



