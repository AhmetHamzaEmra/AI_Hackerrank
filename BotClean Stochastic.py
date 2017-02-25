#!/bin/python3
def nextMove(posr, posc, board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]=='d':
                x=j
                y=i
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

       
        #print ""
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    #print(board)
    nextMove(pos[0], pos[1], board)
