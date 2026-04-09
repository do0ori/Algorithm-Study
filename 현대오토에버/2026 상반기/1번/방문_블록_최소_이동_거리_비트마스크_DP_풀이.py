def solution(w, h, targets):
    # targets는 방문해야 할 블록 번호들 (오름차순, 1 포함)
    n = len(targets)

    def get_pos(x):
        x -= 1
        return x // w, x % w

    # 각 target의 좌표 미리 계산
    pos = [get_pos(x) for x in targets]

    # target들 사이 거리 행렬
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        r1, c1 = pos[i]
        for j in range(n):
            r2, c2 = pos[j]
            dist[i][j] = abs(r1 - r2) + abs(c1 - c2)

    # 시작점 1의 인덱스
    start = targets.index(1)

    INF = float("inf")
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1 << start][start] = 0

    for mask in range(1 << n):
        for i in range(n):
            if dp[mask][i] == INF:
                continue

            for j in range(n):
                if mask & (1 << j):
                    continue
                new_mask = mask | (1 << j)
                dp[new_mask][j] = min(dp[new_mask][j], dp[mask][i] + dist[i][j])

    full_mask = (1 << n) - 1
    return min(dp[full_mask])
