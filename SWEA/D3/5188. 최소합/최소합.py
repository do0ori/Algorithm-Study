def dfs_min(position, total, min_total):
    if min_total <= total:  # 가지치기
        return min_total

    r, c = position
    if position == (N - 1, N - 1):  # 종료조건 = 오른쪽 아래 도달
        return min(min_total, total + numbers[r][c])

    for dr, dc in [(0, 1), (1, 0)]:
        nr, nc = r + dr, c + dc

        if 0 <= nr < N and 0 <= nc < N:
            min_total = dfs_min((nr, nc), total + numbers[r][c], min_total)

    return min_total


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    answer = dfs_min((0, 0), 0, 10 * N * N)

    print(f"#{test_case} {answer}")
