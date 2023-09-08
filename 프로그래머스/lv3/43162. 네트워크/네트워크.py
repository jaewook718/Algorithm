from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers, n)
            answer += 1
    return answer

def bfs(x, visited, computers, n):
    q = deque()
    q.append(x)
    visited[x] = 1
    while q:
        node = q.popleft()
        for j in range(n):
            if computers[node][j] and not visited[j]:
                q.append(j)
                visited[j] = 1