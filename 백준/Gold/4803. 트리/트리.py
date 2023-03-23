from collections import deque

def bfs(i):
    flag = True
    q = deque()
    q.append(i)

    while q:
        x = q.popleft()

        if visited[x] == 1:
            flag = False

        visited[x] = 1
        for y in tree[x]:
            if visited[y] == 0:
                q.append(y)

    return flag

tc = 1
while True:

    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    tree = [[] for _ in range(n+1)]
    for _ in range(m):
        start, end = map(int,input().split())
        tree[start].append(end)
        tree[end].append(start)

    cnt = 0
    visited = [0]*(n+1)
    for i in range(1,n+1):
        if visited[i] == 0:
            c = bfs(i)
            if c == True:
                cnt += 1

    if cnt == 0:
        print(f'Case {tc}: No trees.')
    elif cnt == 1:
        print(f'Case {tc}: There is one tree.')
    else:
        print(f'Case {tc}: A forest of {cnt} trees.')

    tc += 1
