from collections import deque

di = [1,-1,0,0]
dj = [0,0,1,-1]


def melt():
    tmp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                water = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        if not arr[ni][nj]:
                            water += 1
                if arr[i][j] - water > 0:
                    tmp[i][j] = arr[i][j] - water
                else:
                    tmp[i][j] = 0

    return tmp

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0<=nx<N and 0<=ny<M:
                if not visited[nx][ny] and arr[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 1
while True:
    arr = melt()
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    melt()
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    if cnt == 0:
        print(0)
        break
    elif cnt > 1:
        print(ans)
        break
    ans += 1
