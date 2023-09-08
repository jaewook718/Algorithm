from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and maps[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    answer = visited[n-1][m-1]
    if answer == 0:
        answer = -1
    return answer