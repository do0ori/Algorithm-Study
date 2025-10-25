def solution(A, B):
    A.sort()
    B.sort()
    i = j = 0
    score = 0
    n = len(A)

    # A의 i번째를 이길 수 있는 가장 작은 B[j]를 찾는다
    while i < n and j < n:
        if B[j] > A[i]:
            score += 1
            i += 1
            j += 1
        else:
            # 이 B[j]는 어떤 A도 못 이김 → 버리고 다음 B
            j += 1
    return score
