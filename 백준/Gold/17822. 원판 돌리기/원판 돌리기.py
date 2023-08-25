from collections import deque
# xi 원판 di 방향 0 : 시계 1 : 반시계  ki : 칸수
da = [1, 0, -1, 0]
db = [0, 1, 0, -1]


def rotate_right(q):
    q.appendleft(q.pop())


def rotate_left(q):
    q.append(q.popleft())


def bfs(d, x, y):
    q = deque()
    q.append((x, y, d[x][y]))
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1
    tmp = []
    tmp.append((x, y))
    while q:
        a, b, num = q.popleft()
        for k in range(4):
            na = a + da[k]
            nb = (b + db[k])%M
            if 0<=na<N and d[na][nb] == num and not visited[na][nb]:
                q.append((na, nb, num))
                visited[na][nb] = 1
                tmp.append((na, nb))
    count = 0
    if len(tmp) > 1:
        count = 1
        for x, y in tmp:
            d[x][y] = 0
    return d, count


def erase(d):
    count = 0
    for i in range(N):
        for j in range(M):
            if d[i][j] != 0:
                d, tmp = bfs(d, i, j)
                count += tmp

    if count == 0:
        _sum = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if d[i][j]:
                    _sum += d[i][j]
                    cnt += 1
        if _sum > 0:
            avg = _sum/cnt
            for i in range(N):
                for j in range(M):
                    if d[i][j]:
                        if d[i][j]>avg:
                            d[i][j] -= 1
                        elif d[i][j] < avg:
                            d[i][j] += 1
    return d








N, M, T = map(int, input().split())
disk = []
for _ in range(N):
    disk.append(deque(map(int, input().split())))

command = []
for _ in range(T):
    x, d, k = map(int, input().split())
    command.append((x, d, k))

for x, d, k in command:
    for i in range(x, N+1, x):
        for _ in range(k):
            if d == 0:
                rotate_right(disk[i-1])
            else:
                rotate_left(disk[i-1])

    disk = erase(disk)
ans = 0
for i in range(N):
    ans += sum(disk[i])
print(ans)
