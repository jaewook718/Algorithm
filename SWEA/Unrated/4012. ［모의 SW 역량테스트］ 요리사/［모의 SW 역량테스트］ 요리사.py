T = int(input())
def dfs(n):
    global _min
    if n == N//2:
        cnt_1 = 0
        cnt_2 = 0
        for i in range(N):
            if i not in arr:
                arr_2.append(i)
        for i in range(n-1):
            for j in range(i, n):
                cnt_1 += graph[arr[i]][arr[j]] + graph[arr[j]][arr[i]]
                cnt_2 += graph[arr_2[i]][arr_2[j]] + graph[arr_2[j]][arr_2[i]]

        if abs(cnt_1 - cnt_2) < _min:
            _min = abs(cnt_1 - cnt_2)
        arr_2.clear()
        return
    else:
        for i in range(N):
            if i in arr:
                continue

            if len(arr)>0 and arr[len(arr) - 1] > i:
                continue
            arr.append(i)
            dfs(n+1)
            arr.pop()
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    arr = []
    arr_2 = []
    _min = 1e9
    dfs(0)
    print(f'#{tc} {_min}')