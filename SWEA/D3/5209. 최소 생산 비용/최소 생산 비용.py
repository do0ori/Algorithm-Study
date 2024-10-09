def dfs_min(product, total, min_total):
    if min_total <= total:  # 가지치기
        return min_total

    if product == N:  # 종료 조건
        return min(min_total, total)

    for factory in range(N):
        if not visited[factory]:
            visited[factory] = True
            min_total = dfs_min(product + 1, total + cost[product][factory], min_total)
            visited[factory] = False

    return min_total


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    min_cost = dfs_min(0, 0, 99 * N)

    print(f"#{test_case} {min_cost}")
