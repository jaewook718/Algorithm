di = [1,0,-1,0]
dj = [0,-1,0,1]
def bfs():
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni<N and 0<=nj<M and tomato[ni][nj] == 0:
                q.append((ni,nj))
                tomato[ni][nj] = tomato[i][j] + 1

from collections import deque
q = deque()
M, N = map(int,input().split())

tomato = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j))
bfs()
flag = 1
_max = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            flag = 0
            break
        elif _max < tomato[i][j]:
            _max = tomato[i][j]
if flag == 1:
    print(_max-1)
else:
    print(-1)
