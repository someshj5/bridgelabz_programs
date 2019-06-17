N = 1000              # Prime numbers till 1000 asssigned in a variable
primeArr = []         # creating a empty array for prime numbers


def getprime(N,primeArr):  # Function to get the prime numbers till 1000
    for num in range(0, N + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                # print(num)
                primeArr.append(num)
    # print(primeArr)


getprime(1000, primeArr)  # Function to call

blocks = []            # assigning the empty array
k = 0                  # Initialize range to 0
for i in range(0,10): # For loop to iterate through range10 and appending arrays of range 10
    blocks.append([])
    min = k
    k = k+100
    for j in primeArr:  # iterate through prime numbers array to display a range of 100 prime numbers
        if j <= k and j>= min:
            blocks[i].append(j)

for i in blocks:
    print(i)

