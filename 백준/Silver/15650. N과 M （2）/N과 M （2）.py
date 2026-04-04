N, M = map(int, input().split())


def dfs(subset, i=0):
    if i == N:
        if len(subset) == M:
            print(*subset)
        return

    dfs(subset + [i + 1], i + 1)
    dfs(subset, i + 1)


dfs([])
