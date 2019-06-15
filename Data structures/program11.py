N = 1000
primeArr = []


def getprime(N,primeArr):
    for num in range(0, N + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                # print(num)
                primeArr.append(num)
    # print(primeArr)


getprime(1000, primeArr)

blocks = []
k = 0
for i in range(0,10):
    blocks.append([])
    min = k
    k = k+100
    for j in primeArr:
        if j <= k and j>= min:
            blocks[i].append(j)

for i in blocks:
    print(i)

