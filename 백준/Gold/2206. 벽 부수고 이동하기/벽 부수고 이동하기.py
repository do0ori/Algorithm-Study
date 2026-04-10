import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]

q = deque()
q.append((0, 0, 0, 1))  # r, c, 벽 부순 여부(0 or 1), 거리

visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while q:
    r, c, broken, dist = q.popleft()

    if r == N - 1 and c == M - 1:
        print(dist)
        break

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if 0 <= nr < N and 0 <= nc < M:
            # 다음 칸이 길인 경우
            if board[nr][nc] == 0 and not visited[nr][nc][broken]:
                visited[nr][nc][broken] = True
                q.append([nr, nc, broken, dist + 1])
            # 다음 칸이 벽이고, 아직 안 부쉈다면
            elif board[nr][nc] == 1 and broken == 0 and not visited[nr][nc][1]:
                visited[nr][nc][1] = True
                q.append([nr, nc, 1, dist + 1])
else:
    print(-1)
