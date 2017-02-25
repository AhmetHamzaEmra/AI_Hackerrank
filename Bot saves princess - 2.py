def nextMove(n,r,c,grid):
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
        return('LEFT')
    elif mx<px:
        return("RIGHT")
    if my>py:
        return("UP")
    elif py>my:
        return("DOWN")
    
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
