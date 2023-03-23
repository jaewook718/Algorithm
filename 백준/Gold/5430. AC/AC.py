from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    command = list(input())
    n = int(input())
    nums = deque(input().rstrip()[1:-1].split(","))
    count = 0
    if n==0:
        nums = deque()
    for com in command:
        if com == 'R':
            count += 1
        elif com == 'D':
            if nums:
                if count % 2 == 1:
                    nums.pop()
                else:
                    nums.popleft()
            else:
                print('error')
                break

    else:
        if count % 2 ==1:
            nums.reverse()
        print('[' + ','.join(nums)+']')