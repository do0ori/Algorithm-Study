import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# def bfs_intuitive():
#     visited = [[False] * M for _ in range(N)]
#     visited[0][0] = True
#     q = deque([(0, 0)])
#     step = 0

#     while q:
#         for _ in range(len(q)):
#             r, c = q.popleft()

#             if (r, c) == (N - 1, M - 1):
#                 return step + 1

#             for dr, dc in delta:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] and not visited[nr][nc]:
#                     visited[nr][nc] = True
#                     q.append((nr, nc))

#         step += 1


# print(bfs_intuitive())


def bfs_overwrite():
    q = deque([(0, 0)])

    while q:
        r, c = q.popleft()

        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1:
                maze[nr][nc] = maze[r][c] + 1
                q.append((nr, nc))


bfs_overwrite()
print(maze[N - 1][M - 1])
