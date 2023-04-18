dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def clean(x, y, d):
    for _ in range(4):
        d = (d-1)%4
        nx = x + dx[d]
        ny = y + dy[d]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and not arr[nx][ny]:
            visited[nx][ny] = 1
            return nx, ny, d
    nx = x - dx[d]
    ny = y - dy[d]
    return nx, ny, d
N, M = map(int,input().split())
x, y, d = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
if arr[x][y] == 0:
    visited[x][y] = 1
while True:
    x, y, d = clean(x, y, d)
    if arr[x][y] == 1:
        break
ans = 0
for vist in visited:
    for v in vist:
        if v==1:
            ans +=1
print(ans)