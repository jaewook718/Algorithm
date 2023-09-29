import heapq

def solution(n, works):
    if n >= sum(works):
        return 0
    
    works = [-work for work in works]
    heapq.heapify(works)
    for _ in range(n):
        heapq.heappush(works, heapq.heappop(works)+1)
    answer = 0
    for work in works:
        answer += work**2
    return answer