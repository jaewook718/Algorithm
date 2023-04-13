def checkrow(x, a):
    for i in range(9):
        if arr[x][i] == a:
            return False
    return True

def checkcol(y, a):
    for i in range(9):
        if arr[i][y] == a:
            return False
    return True

def checkbox(x, y, a):
    for i in range(3):
        for j in range(3):
            if arr[x//3*3 + i][y//3*3 + j] == a:
                return False
    return True

def dfs(cnt):
    if cnt == len(blank):
        for a in arr:
            print(*a)
        exit(0)
    for i in range(1, 10):
        x = blank[cnt][0]
        y = blank[cnt][1]
        if checkrow(x, i) and checkcol(y, i) and checkbox(x, y, i):
            arr[x][y] = i
            dfs(cnt+1)
            arr[x][y] = 0


arr = [list(map(int,input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            blank.append((i, j))

dfs(0)