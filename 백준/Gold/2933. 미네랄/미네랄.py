from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    check = [[0]*C for _ in range(R)]
    fall_list = []
    q.append([x, y])
    check[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == R-1:
            return
        if arr[x+1][y] == '.':
            fall_list.append([x, y])
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < R and 0 <= my < C:
                if arr[mx][my] == 'x' and not check[mx][my]:
                    check[mx][my] = 1
                    q.append([mx, my])

    fall(check, fall_list)

def fall(check, fall_list):
    c, flag = 1, 0
    while True:
        for i, j in fall_list:
            if i + c == R-1:
                flag = 1
                break
            if arr[i+c+1][j] == 'x' and not check[i+c+1][j]:
                flag = 1
                break
        if flag:
            break
        c += 1

    for i in range(R-2, -1, -1):
        for j in range(C):
            if arr[i][j] == 'x' and check[i][j]:
                arr[i][j] = '.'
                arr[i+c][j] = 'x'


R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]
N = int(input())
com = list(map(int,input().split()))
for turn in range(N):
    height = R - com[turn]
    if turn%2==0:
        start = 0
        while arr[height][start] == '.':
            start += 1
            if start == C-1:
                break
    else:
        start = C-1
        while arr[height][start] == '.':
            start -= 1
            if start == 0:
                break
    arr[height][start] = '.'
    for k in range(4):
        nx = height+dx[k]
        ny = start+dy[k]
        if 0<=nx<R and 0<=ny<C:
            if arr[nx][ny] == 'x':
                bfs(nx,ny)

for a in arr:
    for b in a:
        print(b, end="")
    print()

