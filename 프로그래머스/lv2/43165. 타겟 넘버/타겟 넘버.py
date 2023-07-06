

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(cnt, cur_sum):
        if cnt == n:
            if cur_sum == target:
                nonlocal answer
                answer += 1
            return
        dfs(cnt+1, cur_sum + numbers[cnt])
        dfs(cnt+1, cur_sum - numbers[cnt])
    dfs(0, 0)
    return answer
    