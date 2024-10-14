def dfs(n, total, numbers, target):
    if n == len(numbers):
        return 1 if total == target else 0
    
    return dfs(n + 1, total + numbers[n], numbers, target) + dfs(n + 1, total - numbers[n], numbers, target)
    

def solution(numbers, target):
    return dfs(0, 0, numbers, target)