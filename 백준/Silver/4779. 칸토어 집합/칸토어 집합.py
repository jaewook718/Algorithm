def cantour(start, mid, end, n):
    if n == 0:
        return

    for i in range(mid, mid+n):
        arr[i] = ' '
    cantour(start, start+n//3, start+n//3*2, n//3)
    cantour(end, end + n // 3, end + n // 3 * 2, n // 3)

while True:
    try:
        N = int(input())
        arr = ['-']*(3**N)
        cantour(0, len(arr)//3, len(arr)//3*2,len(arr)//3)
        for a in arr:
            print(a,end='')
        print()
    except EOFError:
        break



