from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 1:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:
                    arr[nx][ny] += 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
time = 0
while True:
    visited = [[0]*M for _ in range(N)]
    bfs()
    flag = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= 3:
                flag = 1
                arr[i][j] = 0
            elif arr[i][j] == 2:
                arr[i][j] = 1
    if flag == 1:
        time += 1
    else:
        break
print(time)