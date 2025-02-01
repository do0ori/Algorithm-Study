def solution(n, left, right):
    return [max(i // n, i % n) + 1 for i in range(left, right + 1)]
    # return [max(i + 1, j + 1) for j in range(n) for i in range(n)][left:right + 1]    # naive
