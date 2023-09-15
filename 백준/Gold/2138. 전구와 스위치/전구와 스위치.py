
N = int(input())
init = list(map(int, input()))
final = list(map(int, input()))

def change(A, B):
    copy_A = A[:]
    press = 0
    for i in range(1, N):
        if copy_A[i-1] == B[i-1]:
            continue

        press += 1
        for j in range(i-1, i+2):
            if j < N:
                copy_A[j] = 1 - copy_A[j]

    if copy_A == B:
        return press
    else:
        return 1e9

ans = change(init, final)
init[0] = 1 - init[0]
init[1] = 1 - init[1]
ans = min(ans, change(init, final)+1)
if ans != 1e9:
    print(ans)
else:
    print(-1)