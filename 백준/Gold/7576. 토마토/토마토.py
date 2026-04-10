import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

q = deque()
unripe = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))
        elif box[i][j] == 0:
            unripe += 1
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while q:
    r, c = q.popleft()

    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and box[nr][nc] == 0:
            box[nr][nc] = box[r][c] + 1
            q.append((nr, nc))
            unripe -= 1

if unripe:
    print(-1)
else:
    print(box[r][c] - 1)
