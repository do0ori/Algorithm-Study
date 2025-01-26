def solution(s):
    s_sorted = sorted(map(int, s.split()))
    return ' '.join(map(str, [s_sorted[0], s_sorted[-1]]))