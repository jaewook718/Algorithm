import heapq
def solution(operations):
    max_heap = []
    heap = []
    for operation in operations:
        cmd, num = operation.split()
        num = int(num)
        if cmd == "I":
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, [num*-1,num])
        elif cmd == "D":
            if len(heap)==0:
                continue
            if num == -1:
                min_value = heapq.heappop(heap)
                max_heap.remove([min_value*-1,min_value])
            else:
                max_value = heapq.heappop(max_heap)[1]
                heap.remove(max_value)
    if heap:
        return [heapq.heappop(max_heap)[1],heapq.heappop(heap)]
    else:
        return [0, 0]
    return answer