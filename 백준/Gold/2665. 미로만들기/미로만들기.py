from collections import deque


def bfs():
    q= deque()
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if arr[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                if arr[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx,ny))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[-1]*N for _ in range(N)]
bfs()
print(visited[N-1][N-1])

