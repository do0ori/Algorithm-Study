from collections import Counter

def solution(topping):
    result = 0
    topping_cnt = Counter(topping)
    left_topping = set()
    for t in topping:
        left_topping.add(t)
        if topping_cnt[t] == 1:
            del topping_cnt[t]
        else:
            topping_cnt[t] -= 1
        if len(left_topping) == len(topping_cnt.keys()):
            result += 1
        
    return result