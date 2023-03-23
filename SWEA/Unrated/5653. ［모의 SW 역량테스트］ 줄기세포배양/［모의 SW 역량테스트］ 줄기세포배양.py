from collections import deque


dx = [0,1,0,-1]
dy = [1,0,-1,0]


def check():
    while q:
        x, y = q.popleft()
        c = arr[x][y][1]
        # print(x,y,c)
        if c <= 0:
            for a in range(4):
                nx = x + dx[a]
                ny = y + dy[a]
                if 0 <= nx < H and 0 <= ny < W:
                    if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                        arr[nx][ny] = [arr[x][y][0], arr[x][y][0]]
                        visited[nx][ny] = k
                    elif visited[nx][ny] == k and arr[nx][ny] != 0:
                        if arr[nx][ny][0] < arr[x][y][0]:
                            arr[nx][ny] = [arr[x][y][0], arr[x][y][0]]
            if c == -arr[x][y][0]+1:
                arr[x][y] = 0
            else:
                arr[x][y][1] -= 1
        else:
            arr[x][y][1] -= 1


T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    W = M+2*K
    H = N+2*K
    arr = [[0]*W for _ in range(H)]
    visited = [[0]*W for _ in range(H)]
    tmp = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if tmp[i][j] != 0:
                arr[K+i][K+j] = [tmp[i][j], tmp[i][j]]
                visited[K+i][K+j] = 1
    q = deque()
    for k in range(K):
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:
                    q.append((i,j))
        check()
    cnt = 0
    for a in arr:
        # print(*a)
        for x in a:
            if x != 0:
                cnt += 1
    print(f'#{tc} {cnt}')