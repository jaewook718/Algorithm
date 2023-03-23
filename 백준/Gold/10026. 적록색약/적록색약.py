import sys
import queue
sys.setrecursionlimit(1000000)
input = lambda :sys.stdin.readline().rstrip()

n = int(input())

m = [list(input()) for _ in range(n)]

visited = [[False]* n for _ in range(n)]

three_cnt, two_cnt = 0, 0
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    q= queue.Queue()
    q.put([x,y])
    visited[x][y] = True
    current_color = m[x][y]
    while not q.empty() :
        a,b = q.get()
        for k in range(4):
            nx = a+dx[k]
            ny = b+dy[k]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False and m[nx][ny] == current_color:
                visited[nx][ny] = True
                q.put([nx,ny])


def dfs(x,y):
    visited[x][y] =True
    current_color = m[x][y]

    for k in range(4):
        nx = x +dx[k]
        ny = y +dy[k]

        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False and m[nx][ny] == current_color:
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i,j)
            three_cnt+=1

for i in range(n):
    for j in range(n):
        if m[i][j] == 'R' :
            m[i][j] = 'G'

visited = [[False]* n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt+=1

print(three_cnt,two_cnt)