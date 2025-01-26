def solution(A,B):
    answer = 0
    
    for a, b in zip(sorted(A, reverse=True), sorted(B)):
        answer += a * b
    
    return answer