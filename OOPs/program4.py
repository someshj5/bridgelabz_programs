from temp2 import Stock

try:
    st = Stock()
    st.Open()
    print('Enter 1 to print the inventory\nEnter 2 to add items\nEnter 3 to remove items\nEnter 4 to quit')
    User = int(input('Enter a value: '))
    if User == 1:
        st.print()
    if User == 2:
        st.addst()
    if User == 3:
        st.delete()
    if User == 4:
        quit()
except FileExistsError:
    print('File Error')
