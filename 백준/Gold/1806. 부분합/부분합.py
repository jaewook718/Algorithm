N, S = map(int, input().split())
numbers = list(map(int, input().split()))
right = 0
left = 0
_sum = 0
min_length = 1e9
while True:
    if _sum >= S:
        min_length = min(min_length, right-left)
        _sum -= numbers[left]
        left += 1
    elif right == N:
        break
    else:
        _sum += numbers[right]
        right += 1

if min_length == 1e9:
    print(0)
else:
    print(min_length)
