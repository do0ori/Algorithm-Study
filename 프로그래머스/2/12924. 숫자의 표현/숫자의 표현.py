def solution(n):
    answer = 0
    for i in range(1, n + 1):
        # 연속된 i개 자연수의 합
        mid = n // i
        smallest = mid - i // 2 + (0 if i % 2 else 1)
        if smallest > 0 and (2 * int(smallest) + i - 1) / 2 * i == n :
            answer += 1
    
    return answer