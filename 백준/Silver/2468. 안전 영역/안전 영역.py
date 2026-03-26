import sys

input = sys.stdin.readline

N = int(input())
region = [list(map(int, input().split())) for _ in range(N)]


def dfs(i, j, visited):
    stack = [(i, j)]

    while stack:
        ci, cj = stack.pop()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if (
                0 <= ni < N
                and 0 <= nj < N
                and region[ni][nj] > h
                and not visited[ni][nj]
            ):
                visited[ni][nj] = True
                stack.append((ni, nj))


def find_safe(h):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and region[i][j] > h:
                visited[i][j] = True
                dfs(i, j, visited)
                cnt += 1

    return cnt


answer = 0
for h in range(100):
    answer = max(answer, find_safe(h))

print(answer)
