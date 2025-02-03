from collections import Counter
import math


def get_multiset(string):
    string = string.upper()
    alphabet = [chr(i) for i in range(65, 91)]
    
    result = []
    for i in range(len(string) - 1):
        element = string[i:i+2]
        if all([e in alphabet for e in element]):
            result.append(element)
    
    return result


def solution(str1, str2):
    multiset1 = get_multiset(str1)
    multiset2 = get_multiset(str2)
    
    multiset1_cnt = Counter(multiset1)
    multiset2_cnt = Counter(multiset2)
    
    set1, set2 = set(multiset1), set(multiset2)
    if not set1 and not set2: return 65536

    intersection, union = set1 & set2, set1 | set2
    
    numerator = 0
    for i in intersection:
        numerator += min(multiset1_cnt.get(i, 0), multiset2_cnt.get(i, 0))
        
    denominator = 0
    for u in union:
        denominator += max(multiset1_cnt.get(u, 0), multiset2_cnt.get(u, 0))
    
    return math.floor((numerator / denominator) * 65536)