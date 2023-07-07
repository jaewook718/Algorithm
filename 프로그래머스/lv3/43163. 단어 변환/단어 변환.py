from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    visited = [0]*len(words)
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            temp = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp += 1
                if temp == 1:
                    q.append((words[i], cnt+1))
                    visited[i] = 1
    return answer