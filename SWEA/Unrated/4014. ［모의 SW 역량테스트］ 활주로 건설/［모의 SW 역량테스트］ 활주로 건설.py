def check(arr):
    ans = 0
    for i in range(N):
        # print(i)
        cnt = 1
        past = arr[i][0]
        j = 1
        flag = 1
        while j < N:
            # print(i, j, arr[i][j])
            if arr[i][j] == past:
                cnt += 1
            elif arr[i][j] > past:
                if past != arr[i][j] -1:
                    flag = 0
                    break
                if cnt < X:
                    flag = 0
                    break
                else:
                    cnt = 1
            elif arr[i][j] < past:
                if arr[i][j] != past - 1:
                    flag = 0
                    break
                past = arr[i][j]
                for k in range(X):
                    if j + k >= N:
                        flag = 0
                        break
                    else:
                        if past != arr[i][j+k]:
                            flag = 0
                            break
                        cnt = X
                if flag == 0:
                    break
                j += X-1
                cnt -= X
            past = arr[i][j]
            j += 1
        if flag == 1:
            ans += 1
    return ans

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    ans += check(arr)
    arr = list(zip(*arr))
    ans += check(arr)
    print(f'#{tc} {ans}')