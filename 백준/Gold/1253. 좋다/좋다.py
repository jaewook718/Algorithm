n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

cnt = 0

for i in range(n):
    tmp = numbers[:i] + numbers[i+1:]
    start = 0
    end = n - 2
    while start < end:
        result = tmp[start] + tmp[end]
        if result == numbers[i]:
            cnt += 1
            break

        if result < numbers[i]:
            start += 1
        else:
            end -= 1
print(cnt)