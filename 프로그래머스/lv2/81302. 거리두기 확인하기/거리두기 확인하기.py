from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solution(places):
    answer = []
    for p in places:
        c = search(p)
        answer.append(c)
    return answer

def bfs(p, i, j):
    q = deque()
    q.append((i, j))
    visited = [[0] * 5 for _ in range(5)]
    visited[i][j] = 1
    while q:
        x, y = q.popleft()
        if visited[x][y] == 3:
            continue
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                if p[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                if p[nx][ny] == 'P':
                    return 0
    return 1

def search(p):
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                c = bfs(p, i, j)
                if c == 0:
                    return 0
    return 1
    