def star(point, n):
    x, y = point
    if n == 1:
        arr[x][y] = '*'
        return

    for i in range(3):
        for j in range(3):
            if i != 1 or j != 1:
                star((x + i*n//3, y + j*n//3), n//3)

N = int(input())
arr = [[' ']*N for _ in range(N)]
star((0,0), N)
for a in arr:
    for b in a:
        print(b,end='')
    print()