from heapq import heappop, heappush

def dikstra(x):
    distances = [int(1e9)]*N
    distances[x] = 0
    q= []
    heappush(q, [x, distances[x]])
    while q:
        cur_node, cur_dist=heappop(q)
        if distances[cur_node] < cur_dist:
            continue


        for node, node_dist in arr[cur_node]:
            distance = cur_dist + node_dist
            if distance < distances[node]:
                distances[node] = distance
                heappush(q, [node, distance])
    return distances[N-1]

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a-1].append([b-1, c])
    arr[b-1].append([a-1, c])
ans = dikstra(0)

print(ans)

