n = int(input())
skylines = []
for _ in range(n):
    a, b = map(int, input().split())
    skylines.append(b)
skylines.append(0)
stack = [0]
ans = 0
for x in skylines:
    height = x
    while stack[-1] > x:
        if stack[-1] != height:
            ans += 1
            height = stack[-1]
        stack.pop()
    stack.append(x)
print(ans)