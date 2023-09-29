def solution(n, s):
    if n > s:
        return [-1]
    arr = [s//n]*n
    idx = n -1
    for _ in range(s%n):
        arr[idx] += 1
        idx-=1
    return arr