def dfs(cur):
    global flag
    if abs(cur[0]-rock[0]) + abs(cur[1] - rock[1]) <= 1000:
        flag = 1
        return
    else:
        for i in range(n):
            if visited[i] == 0:
                if abs(cur[0] - store[i][0]) + abs(cur[1] - store[i][1]) <= 1000:
                    visited[i] = 1
                    dfs(store[i])

t = int(input())
for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    store.sort(key = lambda x : (x[0], x[1]))
    rock = list(map(int, input().split()))
    visited = [0]*n
    flag = 0
    dfs(home)
    if flag == 0:
        print('sad')
    else:
        print('happy')