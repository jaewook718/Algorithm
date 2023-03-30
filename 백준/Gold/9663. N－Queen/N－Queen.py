def check(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x] - arr[i]) == abs(x - i):
            return False
    return True


def N_queen(n, k):
    global cnt
    if n == k:
        cnt += 1
        return
    else:
        for i in range(n):
            arr[k] = i
            if check(k):
                N_queen(n, k+1)

N = int(input())
cnt = 0
arr = [0]*N
N_queen(N,0)
print(cnt)
