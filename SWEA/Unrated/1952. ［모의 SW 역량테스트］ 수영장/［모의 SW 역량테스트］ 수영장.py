T = int(input())

for tc in range(1, T+1):
    day, month, month_3, year = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [0]*12
    dp[0] = min(arr[0]*day, month, month_3, year)
    dp[1] = min(dp[0] + arr[1]*day, dp[0] + month, month_3, year)
    dp[2] = min(dp[1] + arr[2]*day, dp[1] + month, month_3, year)
    for i in range(3, 12):
        dp[i] = min(dp[i-1] + day*arr[i], dp[i-1] + month, dp[i-3] + month_3, year)
    print(f'#{tc} {dp[11]}')