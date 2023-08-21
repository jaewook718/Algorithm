from heapq import heappush, heappop


N, M, K, X = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    A, B  = map(int, input().split())
    arr[A].append(B)

distances = [int(1e9)]*(N+1)
queue = []
distances[X] = 0

heappush(queue, [distances[X], X])
while queue:
    current_distance, current_destination = heappop(queue)
    if distances[current_destination] < current_distance:
        continue

    for node in arr[current_destination]:
        distance = current_distance + 1
        if distance < distances[node]:
            distances[node] = distance
            heappush(queue, [distance, node])

flag= False
for i in range(1, N+1):
    if distances[i] == K:
        print(i)
        flag = True

if flag == False:
    print(-1)

