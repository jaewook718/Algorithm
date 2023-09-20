N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

ans = []
def dfs(index, tmp1, tmp2):
    if not visited[index]:
        visited[index] = 1
        tmp1.add(index)
        tmp2.add(arr[index]-1)
        dfs(arr[index]-1, tmp1, tmp2)

visited = [0]*N
for i in range(N):
    tmp1 = set()
    tmp2 = set()
    if not visited[i] and i not in ans:
        dfs(i, tmp1, tmp2)
    if tmp1 == tmp2:
        ans += list(tmp1)
    else:
        for t in tmp1:
            visited[t] = 0
ans = sorted(ans)
print(len(ans))
for a in ans:
    print(a+1)