# 1 = 익은 토마토
# 0 = 익지 않은 토마토
# -1 = 토마토 없음
import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]


def bfs():
    q = deque()
    # 익은 토마토 위치 찾아서 q에 넣기
    unripe = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if box[h][n][m] == 1:
                    q.append((h, n, m))
                elif box[h][n][m] == 0:
                    unripe += 1

    while q:
        for _ in range(len(q)):
            h, n, m = q.popleft()
            for dh, dn, dm in [
                (-1, 0, 0),
                (1, 0, 0),
                (0, -1, 0),
                (0, 1, 0),
                (0, 0, -1),
                (0, 0, 1),
            ]:
                nh, nn, nm = h + dh, n + dn, m + dm
                if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and box[nh][nn][nm] == 0:
                    box[nh][nn][nm] = box[h][n][m] + 1
                    q.append((nh, nn, nm))
                    unripe -= 1

    # 안 익은 토마토가 존재하면 -1
    return -1 if unripe > 0 else box[h][n][m] - 1


print(bfs())
