from collections import deque


def check():
    if belt[N-1][0]:
        belt[N-1][0] = 0

def end():
    cnt = 0
    for i in range(2*N):
        if belt[i][1] == 0:
            cnt += 1

    return cnt

N, K = map(int, input().split())

tmp = deque(map(int, input().split()))
belt = []
for i in range(2*N):
    belt.append([0, tmp[i]])

belt = deque(belt)

ans = 1
while True:
    belt.appendleft(belt.pop())
    check()
    for i in range(N-2, -1, -1):
        if belt[i][0] and not belt[i+1][0] and belt[i+1][1] > 0:
            belt[i][0] = 0
            belt[i+1][0] = 1
            belt[i+1][1] -= 1
    check()

    if not belt[0][0] and belt[0][1] > 0:
        belt[0][0] = 1
        belt[0][1] -= 1

    if end() >= K:
        print(ans)
        break

    ans+=1

