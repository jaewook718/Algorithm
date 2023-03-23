import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
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

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, e = map(int, input().split())
distance = [int(1e9)] * (N + 1)
dijkstra(s)
print(distance[e])

