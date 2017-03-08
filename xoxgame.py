### %load xoxgame.py
def Check_win(game):
    if game[0]==game[1] and game[1]==game[2] and (game[2]=='X' or game[2]=='O'):
        if game[2]=='X':
            print("you win")
        else:
            print("You lost!")
    elif game[3]==game[4] and game[4]==game[5] and (game[3]=='X' or game[3]=='O'):
        if game[2]=='X':
            print("you win")
        else:
            print("You lost!")
    elif game[6]==game[7] and game[7]==game[8] and (game[6]=='X' or game[6]=='O'):
        if game[2]=='X':
            print("you win")
        else:
            print("You lost!")
    elif game[0]==game[3] and game[3]==game[6] and (game[3]=='X' or game[3]=='O'):
        if game[2]=='X':
            print("you win")
        else:
            print("You lost!")
    elif game[1]==game[4] and game[4]==game[7] and (game[1]=='X' or game[1]=='O'):
        if game[2]=='X':
            print("you win")
        else:
            print("You lost!")
    elif game[2]==game[5] and game[5]==game[8] and (game[2]=='X' or game[2]=='O'):
        if game[2]=='X':
            print("you win")
        else:
            print("You lost!")
    elif game[0]==game[4] and game[4]==game[8] and (game[4]=='X' or game[4]=='O'):
        if game[2]=='X':
            print("you win")
        else:
            print("You lost!")
    elif game[2]==game[4] and game[4]==game[6] and (game[4]=='X' or game[4]=='O'):
        if game[2]=='X':
            print("you win")
        else:
            print("You lost!")
    else:
        play(game)

        
def AI(game):
    
    if game[0] == 'X' and game[0]==game[1] and game[2]=='_':
        game[2]='O'
        return game
    elif game[1]=='X' and game[1]==game[2] and game[0]=='_':
        game[0]='O'
        return game
    elif game[0]=='X' and game[0]==game[2] and game[1]=='_':
        game[1]='O'
        return game
    elif game[3]=='X' and game[3]==game[5] and game[4]=='_': 
        game[4]='O'
        return game
    elif game[4]=='X' and game[4]==game[5] and game[3]=='_':
        game[3]='O'
        return game
    elif game[3]=='X' and game[3]==game[4] and game[5]=='_':
        game[5]='O'
        return game
    elif game[6]=='X' and game[6]==game[8] and game[7]=='_':
        game[7]='O'
        return game
    elif game[7]=='X' and game[7]==game[8] and game[6]=='_':
        game[6]='O'
        return game
    elif game[6]=='X' and game[6]==game[7] and game[8]=='_':
        game[8]='O'
        return game
    elif game[0]=='X' and game[0]==game[3] and game[6]=='_':
        game[6]='O'
        return game
    elif game[0]=='X' and game[0]==game[6] and game[3]=='_':
        game[3]='O'
        return game
    elif game[6]=='X' and game[6]==game[3] and game[0]=='_':
        game[0]='O'
        return game
    elif game[1]=='X' and game[1]==game[4] and game[7]=='_':    
        game[6]='O'
        return game
    elif game[1]=='X' and game[1]==game[7] and game[4]=='_':
        game[4]='O'
        return game
    elif game[7]=='X' and game[7]==game[4] and game[1]=='_':
        game[1]='O'
        return game
    elif game[2]=='X' and game[2]==game[5] and game[8]=='_':   
        game[8]='O'
        return game
    elif game[2]=='X' and game[2]==game[8] and game[5]=='_':
        game[5]='O'
        return game
    elif game[8]=='X' and game[8]==game[5] and game[2]=='_':
        game[3]='O'
        return game
    elif game[0]=='X' and game[4]==game[0] and game[8]=='_': 
        game[8]='O'
        return game
    elif game[0]=='X' and game[8]==game[0] and game[4]=='_':
        game[4]='O'
        return game
    elif game[8]=='X' and game[4]==game[8] and game[0]=='_':
        game[0]='O'
        return game
    elif game[2]=='X' and game[4]==game[2] and game[6]=='_': 
        game[6]='O'
        return game
    elif game[2]=='X' and game[6]==game[2] and game[4]=='_':
        game[4]='O'
        return game
    elif game[6]=='X' and game[4]==game[6] and game[2]=='_':
        game[2]='O'
        return game
    else :
        for i in range(len(game)):
            if game[i] =='_':
                game[i]='O'
                return game

    
    
def play(game):
    if game.count('_')==0:
        print('It is draw!')
        return
    index=[["1","2","3"],["4","5","6"],["7","8","9"]]
    for i in index:
        print(i)
    print("please chose?")

    next_move=int(input().strip())
    
    if game[next_move-1]=='_':
        game[next_move-1]='X'
    else:
        print("Chose again!")
        play(game)
    
    AI(game)

    for i in range(len(game)):
        if i%3==2:
            print(game[i])
        else:
            print(game[i], end=" ")
    Check_win(game)


def start(game):
    print("Do you want to play? (1 to start and 0 to exit)")
    answer=input().strip()
    if answer=='1':
        play(game)
    elif answer=='0':
        return
    else:
        start()


game=["_","_","_","_","_","_","_","_","_"]
start(game)
