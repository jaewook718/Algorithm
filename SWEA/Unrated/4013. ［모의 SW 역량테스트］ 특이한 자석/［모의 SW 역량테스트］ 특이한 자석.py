from collections import deque
def rotateleft(x):
    x.append(x.popleft())


def rotateright(x):
    x.appendleft(x.pop())


def rotate(x,command):
    qu = deque()
    visited = [0]*4
    visited[x] = 1
    qu.append((x,command))
    while qu:
        a, b = qu.popleft()
        if b == 1:
            rotateright(q[a])
        elif b == -1:
            rotateleft(q[a])
        for i in [1, -1]:
            na = a + i
            if 0<=na<4 and visited[na] == 0:
                if na > a and a in tmp:
                    qu.append((na,-b))
                    visited[na] = 1
                elif na < a and na in tmp:
                    qu.append((na,-b))
                    visited[na] = 1


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    q = []
    ans = 0
    for _ in range(4):
        q.append(deque(list(map(int,input().split()))))
    com = [list(map(int, input().split())) for _ in range(K)]
    for n, c in com:
        tmp = []
        for i in range(3):
            if q[i][2] != q[i+1][-2]:
                tmp.append(i)
        rotate(n-1, c)
    for i in range(4):
        if q[i][0] == 1:
            ans += 2**i
    print(f'#{tc} {ans}')
