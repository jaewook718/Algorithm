N, K = map(int, input().split())

arr = [[0,0]] + [list(map(int, input().split())) for _ in range(N)]
knapsack = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        value = arr[i][1]
        weight = arr[i][0]
        if weight > j:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j], value + knapsack[i-1][j-weight])
print(knapsack[N][K])