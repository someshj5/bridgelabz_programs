def Darray():
    M = int(input('Enter the number of rows: '))
    N = int(input('Enter the number of columns: '))
    my_array = [[1]*M]*N 
    my_array [0][0] = 5
    print my_array
print(Darray())

if __name__ == "__main__":
    import timeit
    print(timeit.Timer(Darray))
    