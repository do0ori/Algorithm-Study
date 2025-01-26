from collections import Counter


def solution(k, tangerine):
    tangerine_cnt = Counter(tangerine)
    
    min_type = 0
    for cnt in sorted(tangerine_cnt.values(), reverse=True):
        k -= cnt
        min_type += 1
        
        if k <= 0:
            break
    
    return min_type