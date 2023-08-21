from heapq import heappush, heappop
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt = 1
while True:
    N = int(input())
    if N == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]

    queue = []
    distances = [[int(1e9)]*(N) for _ in range(N)]
    distances[0][0] = arr[0][0]
    heappush(queue, [distances[0][0], (0, 0)])
    while queue:
        current_distance, current_node = heappop(queue)
        if distances[current_node[0]][current_node[1]] < current_distance:
            continue


        for k in range(4):
            nx = current_node[0] + dx[k]
            ny = current_node[1] + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                distance = current_distance + arr[nx][ny]
                if distance < distances[nx][ny] :
                    distances[nx][ny] = distance
                    heappush(queue, [distance, (nx, ny)])
    print(f"Problem {cnt}: {distances[N-1][N-1]}")
    cnt+=1
