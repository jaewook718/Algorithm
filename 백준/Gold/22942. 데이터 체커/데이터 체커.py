import sys
input = sys.stdin.readline

n = int(input())

_list = [list(map(int, input().split())) for _ in range(n)]
points = []
for i in range(n):
    points.append([_list[i][0]-_list[i][1],i,'('])
    points.append([_list[i][0]+_list[i][1],i,')'])

points.sort(key = lambda x : x[0])
stack = []
for i in range(len(points)):
    if points[i][2] == '(':
        stack.append(points[i])

    elif points[i][2] == ')':
        if stack[-1][1] == points[i][1]:
            stack.pop()
        else:
            print('NO')
            break

else:
    print('YES')