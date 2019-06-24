from temp2 import Stock                          # importing class Stock from temp2

try:
    st = Stock()                                 # object assigning
    st.Open()
    print('Enter 1 to print the inventory\nEnter 2 to add items\nEnter 3 to remove items\nEnter 4 to quit')
    User = int(input('Enter a value: '))           # asks user for input
    if User == 1:                                   # if 1 then print the Stockdata
        st.print()
    if User == 2:                                  # 2 to add stock items
        st.addst()
    if User == 3:                                   # 3 to remove stock items
        st.delete()
    if User == 4:                                   # 4 to quit.
        quit()
except FileExistsError:                          # Exception for json file missing
    print('File Error')
