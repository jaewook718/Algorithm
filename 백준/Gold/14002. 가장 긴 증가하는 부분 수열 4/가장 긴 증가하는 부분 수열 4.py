N = int(input())
A = list(map(int, input().split()))
dp = [1]*N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

_max = max(dp)
sequence = []
for i in range(N-1, -1, -1):
    if _max == dp[i]:
        sequence.append(A[i])
        _max-=1

sequence.reverse()
print(*sequence)