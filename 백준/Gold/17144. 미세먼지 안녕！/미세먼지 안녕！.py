di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def diffusion(arr):
    new_arr = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                cnt = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] != -1:
                        cnt += 1
                        new_arr[ni][nj] += arr[i][j] // 5
                new_arr[i][j] += arr[i][j] - arr[i][j] // 5 * cnt
            elif arr[i][j] == -1:
                new_arr[i][j] = -1
    return new_arr


def circulation(arr):
    x, y = air[0]
    dy = [1,0,-1,0]
    dx = [0,-1,0,1]
    before = 0

    for k in range(4):
        while True:
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if arr[nx][ny] !=-1:
                    before, arr[nx][ny] = arr[nx][ny], before
                    x = nx
                    y = ny
                elif arr[nx][ny] == -1:
                    break
            else:
                break

    x, y = air[1]
    dy = [1,0,-1,0]
    dx = [0,1,0,-1]
    before = 0

    for k in range(4):
        while True:
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < R and 0 <= ny < C:
                if arr[nx][ny] !=-1:
                    before, arr[nx][ny] = arr[nx][ny], before
                    x = nx
                    y = ny
                elif arr[nx][ny] == -1:
                    break
            else:
                break

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
air = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            air.append((i, j))
for _ in range(T):
    arr = diffusion(arr)
    circulation(arr)
ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] >0:
            ans += arr[i][j]

print(ans)