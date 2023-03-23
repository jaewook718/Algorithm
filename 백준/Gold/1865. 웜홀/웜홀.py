import sys
input = sys.stdin.readline

def bell(start):
    distance = [int(1e9)]*(N+1)
    distance[start] = 0
    for i in range(N):
        for edge in edges:
            cur = edge[0]
            next_node = edge[1]
            cost = edge[2]
            if distance[next_node] > cost + distance[cur]:
                distance[next_node] = cost + distance[cur]
                if i == N-1:
                    return True
    return False



TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    flag = bell(1)
    if flag:
        print('YES')
    else:
        print('NO')