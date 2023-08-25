from collections import deque
N, K = map(int, input().split())
visited = [-1] * 100001
visited[N] = 0
q = deque()
q.append(N)
while True:
    x = q.popleft()
    if x == K:
        print(visited[x])
        break

    if 0<=x-1<=100000 and visited[x-1] == -1:
        q.append(x-1)
        visited[x-1] = visited[x]+1

    if 0<=2*x<=100000 and visited[2*x] == -1:
        q.appendleft(2*x)
        visited[2*x] = visited[x]
    
    if 0<=x+1<=100000 and visited[x+1] == -1:
        q.append(x+1)
        visited[x+1] = visited[x] +1
