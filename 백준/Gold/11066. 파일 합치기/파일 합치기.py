import sys
input = sys.stdin.readline

def f(a, b, s, dp) :
    if a == b :
        return 0
    if b - a == 1 :
        return s[b] - s[a-1]
    if dp[a][b] != 0 :
        return dp[a][b]
    
    z = min(f(a, k, s, dp) + f(k+1, b, s, dp) for k in range(a, b)) + (s[b] - s[a-1])
    dp[a][b] = z
    return z
    
def solve() :
    k = int(input())
    arr = [0] + list(map(int, input().split()))
    s = [0] * (k+1)
    
    s[1] = arr[1]
    for i in range(2, k+1) :
        s[i] = s[i-1] + arr[i]
        
    dp = [[0] * (k+1) for _ in range(k+1)]    
    
    print(f(1, k, s, dp))
    
        

for _ in range(int(input())) :
    solve()