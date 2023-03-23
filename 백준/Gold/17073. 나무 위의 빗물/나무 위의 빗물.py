import sys
from collections import deque
input = sys.stdin.readline


def bfs(a):
    cnt = 0
    q = deque()
    q.append(a)
    visited[a] = 1
    while q:
        x = q.popleft()
        if len(tree[x]) <= 1 and x!=1:
            cnt+=1
        for y in tree[x]:
            if visited[y] == 0:
                q.append(y)
                visited[y] = 1
    return cnt


N, W = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
visited = [0]*(N+1)
print(W/bfs(1))