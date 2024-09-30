def dfs_min(row, total, min_total):
    # 가지치기
    if min_total <= total:
        return min_total

    # 종료 조건
    if row == N:
        return min(min_total, total)

    for col in range(N):
        if not visited[col]:
            visited[col] = True
            min_total = dfs_min(row + 1, total + arr[row][col], min_total)
            visited[col] = False

    return min_total


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    answer = dfs_min(0, 0, 100)

    print(f"#{test_case} {answer}")
