from program11 import primeArr, blocks # importing prime numbers array

primearr = primeArr


def Prime_anagram(primearr):   # function to get anagram of prime numbers
    for i in primearr:
        for j in primearr:
            i = str(i)
            j = str(j)
            if sorted(i) == sorted(j):
                # print(i, 'and', j)
                return


Prime_anagram(primeArr)

# ---------------------------********PRIME ANAGRRAMS ARRAY************---------------------
print()
anagrams = []
# not_anagrams = []
for i in range(0, len(blocks)):
    anagrams.append([])
    for j in blocks[i]:
        blocks[i].remove(j)
        for k in blocks[i]:
            j = str(j)
            k = str(k)
            if sorted(j) == sorted(k):
                anagrams[i].append(j)
                anagrams[i].append(k)

print('******************************************************************************')
print('Prime number that are ANAGRAMS are:')
for a in anagrams:
    print(a)

