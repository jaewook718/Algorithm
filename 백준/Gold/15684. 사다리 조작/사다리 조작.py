def check():
    a = 1
    for i in range(1, N+1):
        b = 0
        while b<H:
            if yline[b][a]:
                a+=1
            elif yline[b][a-1]:
                a-=1
            b+=1
        if i != a:
            return False
        a+=1
    return True
# yline = [[0,1,0,1,0]]
def dfs(cnt):
    global ans
    if check():
        # for y in yline:
        #     print(*y)
        ans = min(ans, cnt)
        return
    if cnt > ans:
        return
    if cnt ==3:
        return
    else:
        for i in range(H):
            for j in range(1, N):
                if not yline[i][j] and not yline[i][j-1] and not yline[i][j+1]:
                    yline[i][j] = 1
                    dfs(cnt+1)
                    yline[i][j] = 0


N, M, H = map(int, input().split()) # 세로선 N, 가로선 M, 개수 H
yline = [[0]*(N+1) for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    yline[a - 1][b] = 1
ans = 5
dfs(0)
if ans == 5:
    print(-1)
else:
    print(ans)

