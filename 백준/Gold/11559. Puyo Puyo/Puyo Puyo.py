from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def boom(x, y, visited):
    color = arr[x][y]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    tmp = [(x, y)]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6:
                if arr[nx][ny] == color and not visited[nx][ny]:
                    tmp.append((nx, ny))
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    if len(tmp) >= 4:
        for x, y in tmp:
            arr[x][y] = '.'
        return True

    return False


def drop():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if arr[j][i] != '.' and arr[k][i] == '.':
                    arr[k][i] = arr[j][i]
                    arr[j][i] = '.'


def check():
    visited = [[0]*6 for _ in range(12)]
    flag = False
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.':
                if boom(i, j, visited):
                    flag = True

    if flag:
        drop()
    return flag

arr = [list(input()) for _ in range(12)]
ans = 0
while True:
    flag = False
    if check():
        flag = True
        ans += 1
    else:
        print(ans)
        break