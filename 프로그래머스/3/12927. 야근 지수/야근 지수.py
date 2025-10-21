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

# import heapq

# def solution(n, works):
        