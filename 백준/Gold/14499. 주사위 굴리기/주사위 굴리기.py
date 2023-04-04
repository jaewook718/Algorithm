dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(x, y, c, dice):
    nx = x + dx[c]
    ny = y + dy[c]
    if 0 <= nx < N and 0 <= ny < M:
        if c == 0:
            new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
        elif c == 1:
            new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
        elif c == 2:
            new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
        else:
            new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
        if arr[nx][ny] == 0:
            arr[nx][ny] = new_dice[5]
        else:
            new_dice[5] = arr[nx][ny]
            arr[nx][ny] = 0
        print(new_dice[0])
        return nx, ny, new_dice
    else:
        return x, y, dice

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
com = list(map(int, input().split()))
dice = [0]*6
for c in com:
    x, y, dice = move(x, y, c-1, dice)

