from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def melt():
    while wq1:
        x, y = wq1.popleft()
        arr[x][y] = '.'
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<R and 0<=ny<C and not w_visited[nx][ny]:
                if arr[nx][ny] == '.':
                    wq1.append((nx,ny))
                else:
                    wq2.append((nx,ny))
                w_visited[nx][ny] = 1



def swan():
    while sq1:
        x, y = sq1.popleft()
        if x == swx and y == swy:
            return True
        for k in range(4):
            nx, ny = x +dx[k], y +dy[k]
            if 0<=nx<R and 0<=ny<C and not s_visited[nx][ny]:
                if arr[nx][ny] == '.':
                    sq1.append((nx, ny))
                else:
                    sq2.append((nx,ny))
                s_visited[nx][ny] = 1

R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]
wq1, wq2, sq1, sq2 = deque(), deque(), deque(), deque()
ans, swx, swy = 0, 0, 0
w_visited = [[0]*C for _ in range(R)]
s_visited = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'L':
            if not sq1:
                sq1.append((i, j))
                s_visited[i][j] = 1
                arr[i][j] = '.'
            else:
                swx, swy = i, j
                arr[i][j] = '.'

        if arr[i][j] == '.':
            w_visited[i][j] = 1
            wq1.append((i, j))

while True:
    melt()
    if swan():
        print(ans)
        break
    wq1=wq2
    sq1=sq2
    wq2, sq2 = deque(), deque()
    ans+=1



