from heapq import heappush, heappop

def dikstra(start):
    distances = [int(1e9)]*n
    distances[start] = 0
    queue = []
    heappush(queue, (distances[start], start))
    while queue:
        cur_dist, cur_loc = heappop(queue)
        if distances[cur_loc] < cur_dist:
            continue
        for node, l in graph[cur_loc]:
            distance = l + cur_dist
            if distance < distances[node]:
                distances[node] = distance
                heappush(queue, (distance, node))
    tmp = 0
    for i in range(len(distances)):
        if distances[i] <= m:
            tmp += items[i]
    return tmp

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

graph = [[] for _ in range(n)]
for _ in range(r):
    a, b, l = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, l))
    graph[b].append((a, l))

ans = 0
for i in range(n):
    ans = max(ans,dikstra(i))
print(ans)
