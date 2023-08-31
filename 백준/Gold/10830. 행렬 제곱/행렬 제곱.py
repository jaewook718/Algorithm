N, B = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

def mul(MA, MB):
    MC = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp += MA[i][k] * MB[k][j]
            MC[i][j] = tmp%1000

    return MC


def divide(matrix, n):
    if n == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j] %= 1000
        return matrix
    elif n == 2:
        return mul(matrix,matrix)
    else:
        tmp = divide(matrix, n//2)
        if n%2:
            return mul(mul(tmp, tmp), matrix)
        else:
            return mul(tmp, tmp)

for row in divide(arr, B):
    print(*row)