from copy import deepcopy


def dfs(cnt, arr):
    global _max
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j]:
                    _max = max(_max, arr[i][j])
    else:
        for i in range(4):
            copy_arr = deepcopy(arr)
            copy_arr = move(copy_arr, i)
            dfs(cnt + 1, copy_arr)


def move(arr, k):
    if k == 0:
        # 오른쪽
        for i in range(N):
            top = N-1
            for j in range(N-2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][top] == 0:
                        arr[i][top] = tmp
                    elif arr[i][top] == tmp:
                        arr[i][top] = tmp*2
                        top -= 1
                    else:
                        arr[i][top-1] = tmp
                        top -= 1

    elif k == 1:
        # 왼쪽
        for i in range(N):
            top = 0
            for j in range(1, N):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[i][top] == 0:
                        arr[i][top] = tmp
                    elif arr[i][top] == tmp:
                        arr[i][top] = tmp * 2
                        top += 1
                    else:
                        arr[i][top+1] = tmp
                        top += 1

    elif k == 2:
        # 위
        for j in range(N):
            top = 0
            for i in range(1, N):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[top][j] == 0:
                        arr[top][j] = tmp
                    elif arr[top][j] == tmp:
                        arr[top][j] = tmp * 2
                        top += 1
                    else:
                        arr[top + 1][j] = tmp
                        top += 1
    else:
        # 아래
        for j in range(N):
            top = N-1
            for i in range(N-2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if arr[top][j] == 0:
                        arr[top][j] = tmp
                    elif arr[top][j] == tmp:
                        arr[top][j] = tmp * 2
                        top -= 1
                    else:
                        arr[top - 1][j] = tmp
                        top -= 1
    return arr


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
_max = 0
dfs(0, arr)
print(_max)