N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

ans = []
def dfs(index, tmp1, tmp2):
    global ans
    if tmp1 == tmp2:
        ans += tmp1
    if not visited[index]:
        visited[index] = 1
        tmp1.append(index)
        tmp2.append(arr[index]-1)
        dfs(arr[index]-1,list(set(tmp1)), list(set(tmp2)))

for i in range(N):
    visited = [0] * N
    if not visited[i] and i not in ans:
        tmp1 = []
        tmp2 = []
        dfs(i, tmp1, tmp2)

ans = sorted(ans)
print(len(ans))
for a in ans:
    print(a+1)