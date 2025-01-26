def solution(n):
    if n == 0:
        return 0
    
    return solution(n // 2) + (1 if n % 2 else 0)