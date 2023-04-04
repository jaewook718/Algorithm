di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(i, j, cnt, cur_sum):
    global _max
    if cnt == 3:
        _max = max(cur_sum, _max)
    else:
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                dfs(ni, nj, cnt+1, cur_sum + arr[ni][nj])
                visited[ni][nj] = 0



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
_max = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 0, arr[i][j])
        visited[i][j] = 0
        tmp = []
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                tmp.append(arr[ni][nj])
            else:
                tmp.append(0)
        _max = max(_max, arr[i][j] + max(tmp[0]+tmp[1]+tmp[2], tmp[0] + tmp[1] + tmp[3], tmp[0] + tmp[2] + tmp[3], tmp[1] + tmp[2] + tmp[3]))
print(_max)