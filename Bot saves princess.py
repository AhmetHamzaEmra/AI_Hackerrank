#!/usr/bin/python
def displayPathtoPrincess(n,grid):
    mx=-1
    my=-1
    px=-1
    py=-1
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]=='m':
                mx=j
                my=i
            elif grid[i][j]=='p':
                px=j
                py=i
    if mx>px:
        for i in range(mx-px):
            print('LEFT')
    elif mx<px:
        for i in range(px-mx):
            print("RIGHT")
    if my>py:
        for i in range(my-py):
            print("UP")
    elif py>my:
        for i in range(py-my):
            print("DOWN")
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(list(input().strip()))
#print(grid)
displayPathtoPrincess(m,grid)
