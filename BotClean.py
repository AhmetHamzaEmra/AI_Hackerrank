import math
# Head ends here
def next_move(posr, posc, board):
    x=-1
    y=-1
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]=='d':
                x=j
                y=i
                break
        if x>-1 and y>-1:
            break
    #print(x,y)
    if posr>y:
        print("UP")
    elif posr<y:
        print("DOWN")
    else:
        if posc>x:
            print("LEFT")
        elif posc<x:
            print("RIGHT")
        else:
            print("CLEAN")
# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    (next_move(pos[0], pos[1], board))
