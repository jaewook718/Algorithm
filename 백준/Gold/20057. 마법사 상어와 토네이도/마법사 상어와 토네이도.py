dust_ratio = [[[0, 0, 2, 0, 0],
              [0, 10, 7, 1, 0],
              [5, 0, 0, 0, 0],
              [0, 10, 7, 1, 0],
              [0, 0, 2, 0, 0]],

              [[0, 0, 0, 0, 0],
               [0, 1, 0, 1, 0],
               [2, 7, 0, 7, 2],
               [0, 10, 0, 10, 0],
               [0, 0, 5, 0, 0]],

              [[0, 0, 2, 0, 0],
               [0, 1, 7, 10, 0],
               [0, 0, 0, 0, 5],
               [0, 1, 7, 10, 0],
               [0, 0, 2, 0, 0]],

              [[0, 0, 5, 0, 0],
               [0, 10, 0, 10, 0],
               [2, 7, 0 ,7, 2],
               [0, 1, 0, 1, 0],
               [0, 0, 0, 0, 0]]
]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def clean(x2, y2, k):
    dust = arr[x2][y2]
    arr[x2][y2] = 0
    _sum = 0
    out = 0
    for i in range(5):
        for j in range(5):
            sx = x2 + i - 2
            sy = y2 + j - 2
            if 0 <= sx < N and 0 <= sy < N:
                tmp = dust*dust_ratio[k][i][j]//100
                arr[sx][sy] += tmp
                _sum += tmp
            else:
                out += dust*dust_ratio[k][i][j]//100
    rest = dust - _sum - out
    ex = x2 + dx[k]
    ey = y2 + dy[k]
    if 0<=ex<N and 0<=ey<N:
        arr[ex][ey] += rest
    else:
        out += rest
    return out


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
x = y = N//2
visited[x][y] = 1
k = 0
ans = 0
while True:
    while True:
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny]:
                ans += clean(nx, ny, k)
                x, y = nx, ny
                visited[x][y] = 1
                k = (k+1) % 4
                # for a in arr:
                #     print(*a)
                #
                # print()
                break
            else:
                k = (k-1) % 4
        else:
            k = (k+1) % 4

    if x==0 and y==0:
        break
print(ans)

