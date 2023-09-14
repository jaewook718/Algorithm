N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N-1
ans = int(1e11)
left_ans = 0
right_ans = N-1
while left < right:
    tmp = arr[left] + arr[right]
    if abs(tmp) < ans:
        left_ans = left
        right_ans = right
        ans = abs(tmp)

    if tmp == 0:
        break
    elif tmp > 0:
        right -= 1
    else:
        left += 1
print(arr[left_ans], arr[right_ans])