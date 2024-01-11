import sys

M = int(input())
temp = set()
for _ in range(M):
    _input = sys.stdin.readline().strip().split()
    if len(_input) == 1:
        com = _input[0]
        if com == 'all':
            temp = set(x for x in range(1, 21))
        elif com == 'empty':
            temp = set()
    else:
        com = _input[0]
        num = int(_input[1])
        if com == 'add':
            temp.add(num)
        elif com == 'remove':
            temp.discard(num)
        elif com == 'check':
            if num in temp:
                print(1)
            else:
                print(0)
        elif com == 'toggle':
            if num in temp:
                temp.discard(num)
            else:
                temp.add(num)
