import sys

input = sys.stdin.readline

N, M = map(int, input().split())
# 0: 북, 1: 동, 2: 남, 3: 서
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

stack = [(r, c, d)]
clean = 0

while stack:
    i, j, d = stack.pop()

    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if board[i][j] == 0:
        clean += 1
        board[i][j] = -1

    for _ in range(4):
        d = (d + 3) % 4  # 반시계 방향으로 90도 회전한다.
        di, dj = direction[d]
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == 0:
            stack.append((ni, nj, d))
            break
    else:
        # 청소되지 않은 빈 칸이 없는 경우,
        di, dj = direction[(d + 2) % 4]  # 바라보는 방향을 유지한 채로 한 칸 후진
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 1:
            stack.append((ni, nj, d))
        else:  # 후진할 수 없다면 작동을 멈춘다.
            break

print(clean)
