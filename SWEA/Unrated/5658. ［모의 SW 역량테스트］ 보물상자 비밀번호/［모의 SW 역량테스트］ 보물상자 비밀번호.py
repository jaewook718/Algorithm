from collections import deque
hex_to_dec = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7,
              '8' : 8, '9' : 9, 'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13,
              'E' : 14, 'F' : 15}

def rotate():
    q.appendleft(q.pop())


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    q = deque(list(input()))
    ans = []
    for _ in range(N//4):
        for i in range(4):
            tmp = 0
            for j in range(N//4):
                x = q.popleft()
                tmp = tmp*16 + hex_to_dec[x]
                q.append(x)
            ans.append(tmp)
        rotate()
    ans.sort(reverse = True)
    print(f'#{tc} {ans[K-1]}')