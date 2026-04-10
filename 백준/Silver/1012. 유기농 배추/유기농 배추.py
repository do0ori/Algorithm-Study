import sys

input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    board = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1

    visited = [[False] * M for _ in range(N)]
    group = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] and not visited[i][j]:
                visited[i][j] = True
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()

                    for dr, dc in d:
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < N
                            and 0 <= nc < M
                            and board[r][c]
                            and not visited[nr][nc]
                        ):
                            visited[nr][nc] = True
                            stack.append((nr, nc))

                group += 1

    print(group)
