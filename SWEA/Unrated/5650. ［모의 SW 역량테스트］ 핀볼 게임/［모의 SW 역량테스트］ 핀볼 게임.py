# (1,0) 밑 (-1,0) 위 (0,1)오른쪽 (0,-1) 왼쪽

block1 = {(1,0) : (0,1), (0,-1) : (-1,0), (-1,0) : (1,0), (0,1) : (0, -1)}
block2 = {(-1,0) : (0, 1), (0,-1) : (1, 0), (1,0) : (-1,0), (0, 1) : (0, -1)}
block3 = {(-1,0) : (0, -1), (0, 1) : (1, 0), (1, 0) : (-1, 0), (0, -1) : (0, 1)}
block4 = {(1, 0) : (0, -1), (0, 1) : (-1, 0), (-1, 0) : (1, 0), (0, -1) : (0, 1)}
block = [block1, block2, block3, block4]

def check(x, y):
    sx, sy = x, y
    _max = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x, y = sx, sy
        cnt = 0
        while True:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == -1 or (nx == sx and ny == sy):
                    break
                elif 1 <= board[nx][ny] <= 4:
                    dx, dy = block[board[nx][ny] - 1][(dx, dy)]
                    cnt += 1
                elif board[nx][ny] == 5:
                    dx, dy = -dx, -dy
                    cnt += 1
                elif 6 <= board[nx][ny] <= 10:
                    nx, ny = wormhole[board[nx][ny]-6][(nx, ny)]
                x, y = nx, ny
            else:
                dx, dy = -dx, -dy
                cnt += 1
                x, y = nx, ny
        if _max < cnt:
            _max = cnt
    return _max


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    tmp = [[] for _ in range(5)]
    wormhole = [[] for _ in range(5)]
    for i in range(N):
        for j in range(N):
            if 6 <= board[i][j] <= 10:
                tmp[board[i][j] - 6].append((i,j))
    for i in range(5):
        if tmp[i]:
            wormhole[i] = {tmp[i][0] : tmp[i][1], tmp[i][1] : tmp[i][0]}

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                cnt = check(i, j)
                if cnt > ans:
                    ans = cnt
    print(f'#{tc} {ans}')