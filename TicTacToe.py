import random
game = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']]
tie_breaker= []
tie = False

def game_playX():
    x = int(input("Enter row number"))
    y= int(input("Enter column number"))
    game[x][y]="X"
    print(game)

def game_playO():
    x = int(input("Enter row number"))
    y = int(input("Enter column number"))
    game[x][y]="0"
    print(game)

def judge(mark):
    for i in range(4):
        if game[i][0] and game[i][1] and game[i][2] == mark:
            print(mark+'won')
            tie_breaker.append('0')

        elif game[0][i] and game[1][i] and game [2][i] == mark:
            print(mark+'won')
            tie_breaker.append('0')
        
        else:
            pass

def askname():
    P1=input('What is your name P1?')
    P2=input('What is your name P2')

    odev= random.randint(1,2)
    if odev==1:
        return P1
    elif odev==2:
        return P2

print(askname()+' starts the game!')

for i in range(9):
    game_playX()
    game_playO()
    




