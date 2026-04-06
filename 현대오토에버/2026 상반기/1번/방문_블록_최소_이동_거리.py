from functools import lru_cache


def solution(w, h, targets):
    """
    방문해야 하는 블록들을 모두 한 번 이상 방문하기 위한 최소 이동 거리 반환

    Parameters:
        w (int): 가로 길이
        h (int): 세로 길이
        targets (list[int]): 방문해야 하는 블록 번호들 (오름차순, 1 포함)

    Returns:
        int: 최소 이동 거리
    """
    n = len(targets)

    def to_pos(x):
        x -= 1
        return x // w, x % w

    coords = [to_pos(x) for x in targets]

    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        r1, c1 = coords[i]
        for j in range(n):
            r2, c2 = coords[j]
            dist[i][j] = abs(r1 - r2) + abs(c1 - c2)

    start = targets.index(1)
    full_mask = (1 << n) - 1

    @lru_cache(None)
    def dfs(mask, cur):
        if mask == full_mask:
            return 0

        best = float("inf")
        for nxt in range(n):
            if mask & (1 << nxt):
                continue
            cand = dist[cur][nxt] + dfs(mask | (1 << nxt), nxt)
            if cand < best:
                best = cand
        return best

    return dfs(1 << start, start)


if __name__ == "__main__":
    print(solution(5, 2, [1]))
    print(solution(5, 2, [1, 4]))
    print(solution(5, 2, [1, 6]))
    print(solution(5, 2, [1, 5, 8]))
    print(solution(5, 2, [1, 4, 6, 10]))
