from collections import deque

def bfs(x):
    q.append(x)
    visited[x] = 1
    _sum = []
    while q:
        y = q.popleft()
        _sum.append(cost[y])
        for j in friend[y]:
            if visited[j] == 0:
                visited[j] = 1
                q.append(j)
    return _sum


N, M, K = map(int, input().split())
cost = [0] + list(map(int, input().split()))
friend = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
q = deque()
_set = []
for i in range(1, N+1):
    if visited[i] == 0:
        tmp = bfs(i)
        _set.append(tmp)


ans = 0
for s in _set:
    ans += min(s)


if ans > K:
    print('Oh no')
else:
    print(ans)