import sys

input = sys.stdin.readline
N = int(input())
map = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]


def dfs(r, c):
    global h
    h += 1
    visited[r][c] = 1
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and map[nr][nc] == "1" and not visited[nr][nc]:
            dfs(nr, nc)


houses = []
for i in range(N):
    for j in range(N):
        if map[i][j] == "1" and not visited[i][j]:
            h = 0
            dfs(i, j)
            houses.append(h)

houses.sort()
print(len(houses))
for house in houses:
    print(house)
