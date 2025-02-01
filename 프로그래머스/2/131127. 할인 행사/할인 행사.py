from collections import Counter


def solution(want, number, discount):
    for w in want:
        if w not in discount:
            return 0
    
    answer = 0
    want_dict = dict(zip(want, number))
    for i in range(len(discount) - 10 + 1):
        d_cnt = Counter(discount[i:i + 10])
        if set(d_cnt.keys()) != set(want):
            continue
        if all([want_dict[w] <= d_cnt[w] for w in want]):
            answer += 1
    
    return answer