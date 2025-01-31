def solution(n,a,b):
    # 0 ~ n - 1
    a, b = a - 1, b - 1
    answer = 1
    while a // 2 != b // 2:
        answer += 1
        a //= 2
        b //= 2

    return answer