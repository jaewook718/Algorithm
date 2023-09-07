N = int(input())
arr = list(map(int, input().split()))
answer = [0]*N
stack = []
for i in range(N):
    while stack:
        if stack[-1][0] < arr[i]:
            stack.pop()
        else:
            answer[i] = stack[-1][1] + 1
            break

    stack.append((arr[i], i))
print(*answer)