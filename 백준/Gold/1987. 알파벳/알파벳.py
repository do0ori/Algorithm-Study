import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(map(lambda x: ord(x) - 65, input().strip())) for _ in range(R)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = set()

def dfs(r, c, mask):
    state = (r, c, mask)
    if state in visited:
        return 0
    visited.add(state)

    best = 1

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            bit = 1 << board[nr][nc]
            if mask & bit:
                continue
            best = max(best, 1 + dfs(nr, nc, mask | bit))

    return best

start = 1 << board[0][0]
print(dfs(0, 0, start))