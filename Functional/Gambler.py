import random
def Gamble():
    stake = int(input('Enter the cash you want to gamble: $'))
    goal =  int(input('Enter the target money : $'))
    NumberOfTurns = int(input('Enter number if trials: '))

    win = 0
    bet = 0

    for i in range(NumberOfTurns):
        cash = stake
        while cash > 0 and cash < goal:
            bet +=1
            if random.randrange(0,2) == 0:
                cash += 1
            else:
               cash -= 1
        if cash == goal:
            win += 1

        print 'win:',str(win)
        print 'bet', str(bet)   


Gamble()
