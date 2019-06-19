import json

def stockrep():

    with open('stock.json', 'r') as f2:
        stock_data = json.load(f2)
        # print(stock_data)
    print('\t\t\t*****STOCK REPORT*****')

    print('STOCK NAME', 'STOCK PRICE', 'NO OF SHARES', 'AMOUNT', sep='\t\t\t')


    for i in range(4):
        s = stock_data["StockName"][i]["Name"]
        a = stock_data["StockName"][i]["price"]
        b = stock_data["StockName"][i]["No of Share"]
        am =stock_data["StockName"][i]["price"] * stock_data["StockName"][i]["No of Share"]
        print(f'{s}\t\t\t\t\t{a}\t\t\t\t\t{b}\t\t\t\t\t\t{am}')

stockrep()