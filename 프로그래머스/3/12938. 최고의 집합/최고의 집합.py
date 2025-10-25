def solution(n, s):
    q, r = divmod(s, n)
    return [-1] if q == 0 else [q] * (n - r) + [q + 1] * r