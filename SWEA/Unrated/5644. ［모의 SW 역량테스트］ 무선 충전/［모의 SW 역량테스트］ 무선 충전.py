dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

def check(x1, y1, x2, y2):
    c1 = []
    c2 = []
    cnt = 0
    for a, b, c, p in AP:
        d1 = abs(x1 - a) + abs(y1 - b)
        d2 = abs(x2 - a) + abs(y2 - b)
        if d1 <= c:
            c1.append(cnt)
        if d2 <= c:
            c2.append(cnt)
        cnt += 1
    c1.sort()
    c2.sort()
    if c1 and c2:
        if c1[-1] == c2[-1]:
            if len(c1) == 1 and len(c2) == 1:
                return AP[c1[-1]][3]//2, AP[c2[-1]][3]//2
            elif len(c1) == 1:
                return AP[c1[-1]][3], AP[c2[-2]][3]
            elif len(c2) == 1:
                return AP[c1[-2]][3], AP[c2[-1]][3]
            else:
                if AP[c1[-2]][3] > AP[c2[-2]][3]:
                    return AP[c1[-2]][3], AP[c2[-1]][3]
                else:
                    return AP[c1[-1]][3], AP[c2[-2]][3]
        else:
            return AP[c1[-1]][3], AP[c2[-1]][3]
    if c1:
        return AP[c1[-1]][3], 0
    if c2:
        return 0, AP[c2[-1]][3]
    return 0, 0






T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    route1 = list(map(int, input().split()))
    route2 = list(map(int, input().split()))
    AP = [list(map(int, input().split())) for _ in range(A)]
    AP.sort(key= lambda x : x[3])
    p1x, p1y = 1, 1
    p2x, p2y = 10, 10
    ans = 0
    p1, p2 = check(p1x, p1y, p2x, p2y)
    ans += p1 + p2
    for i in range(M):
        p1x = p1x + dx[route1[i]]
        p1y = p1y + dy[route1[i]]
        p2x = p2x + dx[route2[i]]
        p2y = p2y + dy[route2[i]]
        p1, p2 = check(p1x, p1y, p2x, p2y)
        ans += p1 + p2
    print(f'#{tc} {ans}')