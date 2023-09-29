import heapq
def solution(operations):
    heap = []
    for operation in operations:
        cmd, num = operation.split()
        num = int(num)
        if cmd == "I":
            heapq.heappush(heap, num)
        elif cmd == "D":
            if len(heap)==0:
                continue
            if num == -1:
                min_value = heapq.heappop(heap)
            else:
                max_value = max(heap)
                heap.remove(max_value)
    if heap:
        return [max(heap),heapq.heappop(heap)]
    else:
        return [0, 0]
    return answer
