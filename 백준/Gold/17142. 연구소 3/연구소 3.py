from collections import deque
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
selected = [0]*10
dx, dy = [1,-1,0,0], [0,0,1,-1]
virus, vacnt, ret = [], 0, int(1e9)

def bfs(active):
    global ret
    infect, times = 0, 0
    q = deque()
    visited = [[-1]* N for _ in range(N)]
    for x, y in active:
        q.append((x,y))
        visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == -1:
                if board[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                    if board[nx][ny] == 0:
                        infect += 1
                        times = visited[nx][ny]

    if infect == vacnt:
        ret = min(ret, times)

def comb(idx, cnt, v):
    if cnt == M:
        active = []
        for i in range(v):
            if selected[i]:
                x, y = virus[i]
                active.append((x, y))
        bfs(active)
        return
    for i in range(idx, v):
        if not selected[i]:
            selected[i] = 1
            comb(i+1, cnt+1, v)
            selected[i] = 0


for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 0:
            vacnt += 1

comb(0, 0, len(virus))

if ret == int(1e9):
    print(-1)
else:
    print(ret)

