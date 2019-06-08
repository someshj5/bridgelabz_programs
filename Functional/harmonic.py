def HarmonicValue():
    num = int(input('Enter the number to find the harmonic :'))
    harmonic = 1
    for i in range(2,num):
        harmonic += 1/i
        return (harmonic)   
print(HarmonicValue())