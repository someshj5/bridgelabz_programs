def powerOfTwo():
    number = int(input('Please enter a number: '))
    if number >= 31:
        print('Error enter a value below 31')
    else:
        result = list(map(lambda x : 2**x,range(number+1)))


        print('The total term is: ',number+1)
        for i in range(number+1):
            print('2 raised to the power', i ,'is',result[i]  )         


print(powerOfTwo())

