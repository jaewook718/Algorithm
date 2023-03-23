T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    _min = 1e9
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for a in range(0, i+1):
                for b in range(M):
                    if arr[a][b] != 'W':
                        cnt += 1
            for a in range(i+1, j+1):
                for b in range(M):
                    if arr[a][b] != 'B':
                        cnt += 1
            for a in range(j+1, N):
                for b in range(M):
                    if arr[a][b] != 'R':
                        cnt += 1
            if _min > cnt:
                _min = cnt

    print(f'#{tc} {_min}')