from itertools import combinations

def solution(friends, gifts):
    send_log = {f: {} for f in friends} # 누구에게 몇 번 줬는지 기록
    gift_score = {f: {"send_cnt": 0, "receive_cnt": 0} for f in friends}    # 선물 지수에 필요한 값 기록
    for gift in gifts:
        sender, recipient = gift.split()
        send_log[sender][recipient] = send_log[sender].get(recipient, 0) + 1
        gift_score[sender]["send_cnt"] += 1
        gift_score[recipient]["receive_cnt"] += 1
    
    # 선물 지수 계산
    for f in friends:
        gift_score[f] = gift_score[f]["send_cnt"] - gift_score[f]["receive_cnt"]
    
    # 다음 달에 선물 받는 횟수
    result = {f: 0 for f in friends}
    for f1, f2 in combinations(friends, 2):
        g1, g2 = send_log[f1].get(f2, 0), send_log[f2].get(f1, 0)
        if (g1 or g2) and (g1 != g2): # 서로 선물을 주고 받은 기록이 있고 주고받은 수가 다른 경우
            result[f1 if g1 > g2 else f2] += 1  # 더 많이 준 사람이 받기
        else:   # 서로 선물을 주고 받은 기록이 하나도 없거나 주고받은 수가 같은 경우
            gs1, gs2 = gift_score[f1], gift_score[f2]
            if gs1 != gs2:    # 선물 지수가 다른 경우
                result[f1 if gs1 > gs2 else f2] += 1 # 선물 지수가 더 큰 사람이 받기
    
    return max(result.values())
            