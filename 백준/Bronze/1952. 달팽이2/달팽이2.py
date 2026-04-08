import sys

sys.setrecursionlimit(10**6)

M, N = map(int, input().split())

board = [[False] * N for _ in range(M)]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
answer = 0


def dfs(x, y, d):
    global answer

    board[x][y] = True
    dx, dy = direction[d]
    nx, ny = x + dx, y + dy
    if 0 <= nx < M and 0 <= ny < N and not board[nx][ny]:
        dfs(nx, ny, d)
    else:
        d = (d + 1) % 4  # 시계방향으로 90도 회전
        dx, dy = direction[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N and not board[nx][ny]:
            answer += 1
            dfs(x, y, d)
        else:  # 회전해도 못가면 끝
            print(answer)
            return


dfs(0, 0, 0)
