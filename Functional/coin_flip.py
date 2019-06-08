import random

def coinFlip():
    number = int(input('Please enter no of times to flip a coin: '))
    heads = 0
    tails = 0
    for t in range(number):
        flip = random.random()
        if flip > 0.5:
            heads += 1
            
        else:
           
            tails +=1
    print('heads =' ,heads)
    print('tails =',tails)
    print('total heads % =',heads*100//number ,'%')
    print('total tails % =',tails*100//number,'%')
     
print(coinFlip())