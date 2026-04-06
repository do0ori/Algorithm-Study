def solution(powers):
    """
    정확히 1명, 2명, ..., n명의 적을 처치하기 위한 최소 초기 체력을 배열로 반환

    Parameters:
        powers (list[int]): 적 power 배열

    Returns:
        list[int]: answer[k - 1] = 정확히 k명을 처치하기 위한 최소 초기 체력
    """

    positives = sorted(x for x in powers if x > 0)
    negatives = sorted((x for x in powers if x < 0), reverse=True)  # -1, -2, -5, ...

    p_cnt = len(positives)
    n_cnt = len(negatives)
    total = len(powers)

    # prefix sum of positives
    pos_sum = [0] * (p_cnt + 1)
    for i in range(1, p_cnt + 1):
        pos_sum[i] = pos_sum[i - 1] + positives[i - 1]

    # prefix sum of negatives (negative values)
    neg_sum = [0] * (n_cnt + 1)
    for i in range(1, n_cnt + 1):
        neg_sum[i] = neg_sum[i - 1] + negatives[i - 1]

    # need_pos[x]: 앞의 x개 양수 적을 모두 잡기 위한 최소 초기 체력
    # 양수 적 p를 잡으려면 현재 체력 > p 이므로
    # H + prefix_before >= p + 1
    need_pos = [1] * (p_cnt + 1)
    for i in range(1, p_cnt + 1):
        need_here = positives[i - 1] + 1 - pos_sum[i - 1]
        need_pos[i] = max(need_pos[i - 1], need_here, 1)

    # need_neg[y]: 앞의 y개 음수 적을 모두 잡기 위해
    # "음수 구간 시작 직전" 필요한 최소 체력
    # negative = -a 를 잡으려면 현재 체력이 a보다 커야 하고,
    # 잡고 나서도 1 이상이어야 하므로 결국 현재 체력 >= a + 1 이 필요.
    need_neg = [1] * (n_cnt + 1)
    for i in range(1, n_cnt + 1):
        # current_before = S + neg_sum[i - 1]
        # need current_before >= abs(negatives[i - 1]) + 1
        need_here = -negatives[i - 1] - neg_sum[i - 1] + 1
        need_neg[i] = max(need_neg[i - 1], need_here, 1)

    def cost(k, x):
        """
        정확히 k명을 잡을 때,
        양수 x명 + 음수 (k-x)명을 선택했을 때 필요한 최소 초기 체력
        """
        y = k - x
        return max(1, need_pos[x], need_neg[y] - pos_sum[x])

    answer = [0] * total

    for k in range(1, total + 1):
        lo = max(0, k - n_cnt)
        hi = min(k, p_cnt)

        # A(x)=need_pos[x] 는 증가
        # B(x)=need_neg[k-x] - pos_sum[x] 는 감소
        # max(A, B)의 최소는 교차 지점 근처에서 발생
        l, r = lo, hi
        while l < r:
            mid = (l + r) // 2
            if need_pos[mid] >= need_neg[k - mid] - pos_sum[mid]:
                r = mid
            else:
                l = mid + 1

        best = cost(k, l)
        if l > lo:
            prev_cost = cost(k, l - 1)
            if prev_cost < best:
                best = prev_cost

        answer[k - 1] = best

    return answer


if __name__ == "__main__":
    print(solution([1]))
    print(solution([-1]))
    print(solution([2, -1]))
    print(solution([3, 4, -2]))
    print(solution([2, 5, -1, -2]))
    print(solution([14, -10, 3, -2]))
