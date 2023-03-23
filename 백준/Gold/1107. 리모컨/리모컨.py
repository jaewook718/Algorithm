n = int(input())
m = int(input())
if m > 0:
    broken = list(input().split())
else:
    broken = []

min_count = abs(n - 100)
for num in range(1000001):
    for a in str(num):
        if a in broken:
            break
    else:
        if min_count > abs(num - n) + len(str(num)):
            min_count = abs(num -n) + len(str(num))

print(min_count)






