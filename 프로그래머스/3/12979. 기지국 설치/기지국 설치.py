def solution(N, stations, W):
    coverage = 2 * W + 1
    answer = 0
    prev_covered_end = 0  # 직전까지 커버된 마지막 아파트 번호 (1-indexed 기준)

    for s in stations:
        left = max(1, s - W)
        right = min(N, s + W)

        # 직전 커버 끝(prev_covered_end)과 이번 커버 시작(left) 사이의 빈 구간
        gap_len = left - prev_covered_end - 1
        if gap_len > 0:
            answer += (gap_len + coverage - 1) // coverage

        prev_covered_end = right

    # 마지막 커버 뒤에 남은 구간
    if prev_covered_end < N:
        gap_len = N - prev_covered_end
        answer += (gap_len + coverage - 1) // coverage

    return answer
