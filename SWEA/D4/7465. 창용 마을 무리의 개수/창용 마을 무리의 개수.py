from collections import deque

def bfs(i):
    global ans
    if visited[i] == 0:
        ans += 1
    q = deque()
    q.append(i)
    visited[i] = 1
    while q:
        x = q.popleft()
        for y in range(N+1):
            if arr[x][y] == 1 and visited[y] == 0:
                q.append(y)
                visited[y] = 1
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int,input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    visited = [0]*(N+1)
    ans = 0
    for i in range(1, N+1):
        bfs(i)
    print(f'#{tc} {ans}')