from copy import deepcopy
from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def boom(arr, cnt):
    global _min
    if cnt == N:
        count = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:
                    count += 1
        if _min > count:
            _min = count
    else:
        for j in range(W):
            i = 0
            while i < H-1 and arr[i][j] == 0: i += 1
            if arr[i][j] != 0:
                arr_copy = deepcopy(arr)
                bfs(i, j, arr_copy)
                down(arr_copy)
                boom(arr_copy, cnt+1)


def bfs(a, b, arr):
    q.append((a, b))
    while q:
        x, y = q.popleft()
        n = arr[x][y]
        arr[x][y] = 0
        for i in range(4):
            for j in range(n):
                nx = x + dx[i]*j
                ny = y + dy[i]*j
                if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] != 0:
                    q.append((nx, ny))


def down(arr):
    for j in range(W):
        for i in range(H):
            if arr[i][j] == 0 and arr[i-1][j] != 0:
                a, b = i, j
                while a > 0:
                    arr[a][b] = arr[a-1][b]
                    a -= 1
                arr[0][b] = 0


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(H)]
    q = deque()
    _min = 1e9
    boom(board, 0)
    print(f'#{tc}', end = ' ')
    if _min != 1e9:
        print(_min)
    else:
        print(0)