def dfs(numbers, target, n, idx, value):
    answer = 0
    if idx == n:
        if target == value:
            return 1
        else:
            return 0
    
    answer += dfs(numbers, target, n, idx + 1, value + numbers[idx])
    answer += dfs(numbers, target, n, idx + 1, value - numbers[idx])
    return answer

def solution(numbers, target):
    return dfs(numbers, target, len(numbers), 0, 0)