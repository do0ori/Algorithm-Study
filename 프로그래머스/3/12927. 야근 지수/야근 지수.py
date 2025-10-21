from collections import Counter

# def naive_solution(n, works):
#     for _ in range(n):
#         max_work = max(works)
#         if max_work == 0:
#             return 0
#         for i in range(len(works)):
#             if works[i] == max_work:
#                 works[i] -= 1
#                 break
#     return sum([w ** 2 for w in works])

"""
def solution(n, works):
    cnt = Counter(works)
    if sum(works) <= n:
        return 0

    max_k = max(cnt)
    for _ in range(n):
        # 현 시점의 최댓값 찾기 (비어 있으면 한 칸 내림)
        while max_k > 0 and cnt.get(max_k, 0) == 0:
            max_k -= 1
        if max_k == 0:  # 더 줄일 일 없음
            return 0

        # 최댓값 하나 줄이기
        cnt[max_k] -= 1
        cnt[max_k - 1] = cnt.get(max_k - 1, 0) + 1

    # 제곱합
    return sum(k * k * v for k, v in cnt.items() if k > 0)
"""


def solution(n, works):
    total = sum(works)
    if total <= n:
        return 0

    cnt = Counter(works)
    levels = sorted(cnt.keys(), reverse=True)

    # 누적 개수: "현재 최상단 ~ 여기까지" 쌓인 작업 개수
    cum = cnt[levels[0]]

    for i in range(len(levels)):
        h  = levels[i]
        h2 = levels[i + 1] if i + 1 < len(levels) else 0  # 다음 낮은 레벨(없으면 0)

        # 최상단 cum개를 h2까지 내리는 데 필요한 총 시간
        drop_need = (h - h2) * cum

        if n >= drop_need:
            # 전부 h2까지 내릴 수 있음 → 내리고, 다음 레벨까지 누적 확장
            n -= drop_need
            orig_next = cnt.get(h2, 0)
            cnt[h] = 0
            cnt[h2] = orig_next + cum

            if i + 1 < len(levels):
                cum += orig_next
        else:
            # h2까지는 못 내려감 → 남은 n을 cum개에 균등 분배하고 종료
            q, r = divmod(n, cum)     # 모두 q만큼 내리고, r개는 한 번 더 내림
            new_h = h - q

            # cum개 중 r개는 new_h-1, (cum-r)개는 new_h
            sq = r * (new_h - 1) ** 2 + (cum - r) * (new_h) ** 2

            # 아래(더 낮은) 레벨들은 변화 없음 → 그대로 더함
            for j in range(i + 1, len(levels)):
                lv = levels[j]
                sq += cnt[lv] * (lv ** 2)
            return sq

    # 여기까지 왔다는 건 전부 0까지 평탄화됨
    return 0
