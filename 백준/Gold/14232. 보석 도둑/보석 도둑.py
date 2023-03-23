n = int(input())
num = 2
count = 0
_lst = []
for num in range(2, int(n**.5)+1):
    while n % num == 0:
        n = n//num
        count += 1
        _lst.append(num)
    if n == 1:
        break
if n != 1:
    _lst.append(n)
    count+=1

print(count)
print(*_lst)