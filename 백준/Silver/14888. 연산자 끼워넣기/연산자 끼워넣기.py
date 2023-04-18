def dfs(k, cur, plus, minus, mul, div):
    global _max
    global _min
    if k == N:
        _max = max(_max, cur)
        _min = min(_min, cur)
        return
    if plus:
        dfs(k+1, cur+nums[k], plus-1, minus, mul, div)
    if minus:
        dfs(k+1, cur-nums[k], plus, minus-1, mul, div)
    if mul:
        dfs(k+1, cur*nums[k], plus, minus, mul-1, div)
    if div:
        dfs(k+1, int(cur/nums[k]), plus, minus, mul, div-1)


N = int(input())
nums = list(map(int,input().split()))
opperand = list(map(int,input().split()))
# +, -, *, /
_max = -int(1e9)
_min = int(1e9)
dfs(1, nums[0], opperand[0], opperand[1], opperand[2], opperand[3])
print(_max)
print(_min)