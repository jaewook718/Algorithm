num = ['1111110', '0110000', '1101101', '1111001', '0110011', '1011011',
       '1011111', '1110000', '1111111', '1111011']

n, k, p, x = map(int, input().split())

if len(str(x)) < k:
    tmp = '0' * (k-len(str(x))) + str(x)
else:
    tmp = str(x)

arr =[]

for i in range(10):
    arr.append([])
    for j in range(10):
        if i == j:
            arr[i].append(0)
        else:
            d = 0
            for h in range(7):
                if num[i][h] != num[j][h]:
                    d += 1
            arr[i].append(d)
ans = 0


def dfs(dep, cnt, cx):
    global ans
    if dep >= len(cx):
        if int(cx) == x:
            return
        elif 1 <= int(cx) <= n:
            ans += 1
            return
        else:
            return

    cur = int(cx[dep])
    for i in range(10):
        if cur != i and (arr[cur][i] <= cnt):
            dx = cx[:dep] + str(i) + cx[dep+1:]
            dfs(dep+1, cnt-arr[cur][i], dx)
        elif cur == i:
            dfs(dep+1, cnt, cx)

dfs(0,p,tmp)
print(ans)
