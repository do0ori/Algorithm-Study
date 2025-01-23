def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생이 도난당한 경우를 처리
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    # 체육복 빌려주기
    for student in sorted(reserve_set):
        if student - 1 in lost_set:  # 앞번호 학생에게 빌려줌
            lost_set.remove(student - 1)
        elif student + 1 in lost_set:  # 뒷번호 학생에게 빌려줌
            lost_set.remove(student + 1)

    # 전체 학생 수에서 체육복이 없는 학생 수를 뺌
    return n - len(lost_set)

# def solution(n, lost, reserve):
#     sportswear = [1] * (n + 1)
#     for r in reserve: sportswear[r] += 1
#     for l in lost: sportswear[l] -= 1
    
#     min_total = 0
#     for sw in sportswear[1:]:
#         if sw > 0: min_total += 1
            
#     def canBorrowFrom(i):
#         return 1 <= i <= n and sportswear[i] > 1
    
#     def dfs_find_max(i, total, max_total):
#         if i == n + 1:  # 종료 조건
#             return max(total, max_total)

#         # 체육복 있거나 주변에 빌릴 사람 없음
#         if sportswear[i] > 0 or \
#             not canBorrowFrom(i - 1) and not canBorrowFrom(i + 1):
#             # 다음 학생으로 이동
#             max_total = dfs_find_max(i + 1, total, max_total)
#         # 체육복이 없고 주변에 빌릴 사람 있음
#         else:
#             # 앞뒤 학생에게 체육복 빌리기
#             for adj in [i - 1, i + 1]:
#                 if canBorrowFrom(adj):
#                         sportswear[adj] -= 1
#                         sportswear[i] += 1
#                         max_total = dfs_find_max(i + 1, total + 1, max_total)
#                         sportswear[adj] += 1
#                         sportswear[i] -= 1
            
#         return max_total
            
#     return dfs_find_max(1, min_total, min_total)