import json                                     # importing json module
from temp2 import Stock                         # importing class Stock from temp2 file


try:
    st = Stock()                               # assinging object to Stock class
    st.Open()
    print('Enter 1 to print the inventory\nEnter 2 to add items\nEnter 3 to remove items\nEnter 4 to quit')
    User = int(input('Enter a value: '))         # Ask for user input
    if User == 1:                                # if 1 the print the inventory
        st.print()
    if User == 2:                                # for 2 adding stock items to the object
        st.addst()
    if User == 3:                               # 3 for removing stock items from the object
        st.delete()
    if User == 4:
        quit()
except FileExistsError:                         # execption handling for json file
    print('File Error')

# --------------------------------- STOCK PRICE CALCULATION ---------------------------------------------


def stockrep():                       # Function to calculate stock amount

    with open('stock.json', 'r') as f2:   # loading json data to a variable
        stock_data = json.load(f2)

        print('\n')
    print('\t\t\t*****STOCK REPORT*****')          # printing table for stock report

    print('STOCK NAME' ,'STOCK PRICE|', 'NO OF SHARES|', 'AMOUNT', sep='\t\t\t')
    print('*********************************************************************************')

    for i in range(4):
        s = stock_data["StockName"][i]["Name"]
        a = stock_data["StockName"][i]["price"]
        b = stock_data["StockName"][i]["No of Share"]
        am =stock_data["StockName"][i]["price"] * stock_data["StockName"][i]["No of Share"]
        print(f'{s}\t\t\t|\t\t{a}\t\t\t|\t\t{b}\t\t\t\t|\t\t{am}')

stockrep()