def dfs(v):
    visited[v] = 1
    for w in range(N):
        if graph[v][w] == 1 and visited[w] == 0:
            dfs(w)


N = int(input())
M = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

route = list(map(int,input().split()))
visited = [0]*N
dfs(route[0] - 1)
if 0 not in visited:
  print('YES')
  exit()
for i in route:
  if visited[i-1]==0:
    print('NO')
    exit()
print('YES')