import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(i, j, visited):
    q = deque([(i, j)])

    while q:
        for _ in range(len(q)):
            r, c = q.popleft()

            for dr, dc in diff:
                nr, nc = r + dr, c + dc
                if iceberg[nr][nc] and visited[nr][nc] == -1:
                    water = 0
                    for dr2, dc2 in diff:
                        nr2, nc2 = nr + dr2, nc + dc2
                        if not iceberg[nr2][nc2]:
                            water += 1
                    visited[nr][nc] = water
                    q.append((nr, nc))


def answer():
    min_day = 0
    while True:
        visited = [[-1] * M for _ in range(N)]
        cnt = 0
        # 그룹 개수 파악 및 녹는 정도 체크
        for i in range(N):
            for j in range(M):
                if cnt >= 2:
                    return min_day
                if iceberg[i][j] and visited[i][j] == -1:
                    bfs(i, j, visited)
                    cnt += 1

        if cnt == 0:
            return 0

        # 녹기 반영
        for i in range(N):
            for j in range(M):
                if visited[i][j] > 0:
                    iceberg[i][j] = max(iceberg[i][j] - visited[i][j], 0)

        min_day += 1


print(answer())
