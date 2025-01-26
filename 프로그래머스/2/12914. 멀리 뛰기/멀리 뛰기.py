def factorial(n):
    result = 1
    i = n
    while i > 1:
        result *= i
        i -= 1
    
    return result

def solution(n):
    answer = 0
    
    for num_2 in range(n // 2 + 1):
        num_1 = n - 2 * num_2
        answer += factorial(num_1 + num_2) // (factorial(num_1) * factorial(num_2))
    
    return answer % 1234567
        