#define function
def SwapNibble(x): 
    #Shfting and swaping of bits
    return ( (x & 0x0F) << 4 | (x & 0xF0) >> 4)


#integer to be converted
x= int(input('Enter a number:'))

 #print result pass x to fuction 
print(SwapNibble(x)) 