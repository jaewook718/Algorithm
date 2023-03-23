from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    flag = 0
    visited[x] = 1
    while q:
        i = q.popleft()
        if flag == 0 and len(tree[i]) > 2:
            ans = visited[i]-1
            flag = 1
        if flag == 0 and len(tree[i]) > 1 and i==x:
            ans = 0
            flag = 1
        for j, k in tree[i]:
            if visited[j] == 0:
                visited[j] = visited[i] + k
                q.append(j)
    if flag == 1:
        return ans, max(visited) - 1 - ans
    else:
        return max(visited)-1, 0

N, root = map(int, input().split())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int,input().split())
    tree[a].append([b,c])
    tree[b].append([a,c])
visited = [0]*(N+1)
i = root
a = bfs(i)
print(*a)


