N, C = map(int, input().split())
home =[]
for _ in range(N):
    home.append(int(input()))
home.sort()

start = 1
end = home[-1] - home[0]
while start <= end:
    global answer
    mid = (start + end) // 2
    count = 1
    current = home[0]
    for i in range(1, N):
        if home[i] >= current + mid:
            count += 1
            current = home[i]

    if count >= C:
        start = mid + 1
        answer = mid

    else:
        end = mid - 1

print(answer)