dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
fire = []
arr = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire.append([r-1, c-1, m, s, d])

for _ in range(K):
    while fire:
        r, c, m, s, d = fire.pop()
        r = (r + dx[d]*s) % N
        c = (c + dy[d]*s) % N
        arr[r][c].append([m, s, d])

    for r in range(N):
        for c in range(N):
            if len(arr[r][c]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(arr[r][c])
                while arr[r][c]:
                    m, s, d = arr[r][c].pop()
                    sum_m += m
                    sum_s += s
                    if d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1

                if cnt_odd == cnt or cnt_even == cnt:
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]

                if sum_m//5:
                    for d in nd:
                        fire.append([r, c, sum_m//5, sum_s//cnt, d])

            elif len(arr[r][c]) == 1:
                fire.append([r, c] + arr[r][c].pop())

ans = 0
for f in fire:
    ans += f[2]

print(ans)