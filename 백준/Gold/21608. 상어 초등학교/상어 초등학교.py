di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

N = int(input())
likes = [[] for _ in range(N**2+1)]

arr = [[0]*N for _ in range(N)]
students = [[] for _ in range(N**2 + 1)]
for _ in range(N**2):
    a, b, c, d, e = map(int, input().split())
    students[a] = [b, c, d, e]
    tmp = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    ni, nj = i+ di[k], j +dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] in [b, c, d, e]:
                            like += 1
                        elif arr[ni][nj] == 0:
                            blank += 1

                tmp.append([like, blank, i, j])
    tmp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    arr[tmp[0][2]][tmp[0][3]] = a

ans = 0

for i in range(N):
    for j in range(N):
        num = arr[i][j]
        tmp = 0
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<=ni <N and 0<=nj < N:
                if arr[ni][nj] in students[num]:
                    tmp += 1
        if tmp == 1:
            ans += 1
        elif tmp == 2:
            ans += 10
        elif tmp == 3:
            ans += 100
        elif tmp == 4:
            ans += 1000

print(ans)
