from collections import defaultdict


def solution(k, tangerine):
    tangerine_cnt = defaultdict(int)
    for t in tangerine:
        tangerine_cnt[t] += 1
    
    min_type = 0
    for size, cnt in sorted(tangerine_cnt.items(), key=lambda x: x[1],reverse=True):
        if k > 0:
            k -= cnt
            min_type += 1
        else:
            break
    
    return min_type