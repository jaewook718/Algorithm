from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        a, b = q.popleft()
        for k in range(4):
            nx, ny = a + dx[k], b + dy[k]
            if 0<=nx<2**N and 0<=ny<2**N:
                if arr[nx][ny] and not visited[nx][ny]:
                    cnt += 1
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    return cnt


def turn(x, y, l):
    tmp = [[0]*(2**l) for _ in range(2**l)]
    for a in range(2**l):
        for b in range(2**l):
            tmp[a][b] = arr[x*(2**l)+(2**l-b-1)][y*(2**l)+a]

    for a in range(2**l):
        for b in range(2**l):
            arr[x*(2**l)+a][y*(2**l)+b] = tmp[a][b]


def melt(x, y):
    cnt = 0
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0<=nx<2**N and 0<=ny<2**N:
            if arr[nx][ny]:
                cnt += 1

    if cnt < 3:
        arr_tmp[x][y] = arr[x][y] - 1
    else:
        arr_tmp[x][y] = arr[x][y]


N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**N)]

if Q == 1:
    com = [int(input())]

else:
    com = list(map(int, input().split()))

for L in com:
    for i in range(2**N//2**L):
        for j in range(2**N//2**L):
            turn(i, j, L)



    arr_tmp = [[0]*2**N for _ in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            if arr[i][j]:
                melt(i, j)

    arr = arr_tmp


visited = [[0]*(2**N) for _ in range(2**N)]
ans = 0
ice = 0
for i in range(2**N):
    for j in range(2**N):
        if arr[i][j] and not visited[i][j]:
            ans = max(ans, bfs(i, j))
        ice += arr[i][j]

print(ice)
print(ans)