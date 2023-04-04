from collections import deque
def move():
    head = q[-1]
    x = head[0] + vector[v][0]
    y = head[1] + vector[v][1]
    head = [x, y]
    if head in q or x < 1 or x > N or y < 1 or y > N:
        return 1
    q.append(head)
    if head not in apple:
        q.popleft()
    else:
        apple.pop(apple.index(head))
    return 0

vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N = int(input())
K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]

L = int(input())
com = [list(input().split()) for _ in range(L)]
v = 0
q = deque()
q.append((1,1))
cnt = 0
for i in range(1, 10000):
    flag = move()
    if flag == 1:
        print(i)
        break
    if i == int(com[cnt][0]):
        if com[cnt][1] == 'D':
            v = (v+1) % 4
        else:
            v = (v-1) % 4
        cnt += 1
    if cnt == L:
        cnt -= 1