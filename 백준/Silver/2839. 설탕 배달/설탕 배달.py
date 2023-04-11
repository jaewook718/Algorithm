N = int(input())
dp = [0]*5001
dp[1] = -1
dp[2] = -1
dp[3] = 1
dp[4] = -1
dp[5] = 1
for i in range(6,N+1):
    if dp[i-3] != -1 and dp[i-5] != -1:
        dp[i] = min(dp[i-3], dp[i-5]) + 1
    elif dp[i-3] == -1 and dp[i-5] != -1:
        dp[i] = dp[i-5] + 1
    elif dp[i-3] != -1 and dp[i-5] == -1:
        dp[i] = dp[i-3] + 1
    else:
        dp[i] = -1
print(dp[N])