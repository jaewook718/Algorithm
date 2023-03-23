import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    distance = [int(1e9)] * (N + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, [distance[start], start])
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for v, w in graph[now]:
            tmp = dist + w
            if tmp < distance[v]:
                distance[v] = tmp
                heapq.heappush(q, (tmp, v))
    return distance

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int,input().split())

d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)

d_1 = d1[v1] + d2[v2] + d3[N]
d_2 = d1[v2] + d3[v1] + d2[N]
result = min(d_1, d_2)
print(result if result < 1e9 else -1)

