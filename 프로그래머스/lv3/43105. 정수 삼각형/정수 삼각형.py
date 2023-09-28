from collections import deque
def dp(triangle):
    ans = [[0]*len(triangle) for _ in range(len(triangle))]
    ans[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                ans[i][j] = ans[i-1][j] + triangle[i][j]
            elif j == i:
                ans[i][j] = ans[i-1][j-1] + triangle[i][j]
            else:
                ans[i][j] = max(ans[i-1][j-1], ans[i-1][j]) + triangle[i][j]
    return max(ans[len(triangle)-1])
            
def solution(triangle):
    answer = dp(triangle)
    return answer