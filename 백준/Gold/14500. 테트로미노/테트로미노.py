import sys

input = sys.stdin.readline

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * M for _ in range(N)]
answer = 0


def tetromino1(r, c, depth, total):
    """
    한 줄로 표현 가능한 테트로미노
    """
    global answer

    if depth == 4:
        answer = max(answer, total)
        return

    for dr, dc in d:
        nr, nc = r + dr, c + dc

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            tetromino1(nr, nc, depth + 1, total + paper[nr][nc])
            visited[nr][nc] = False


def tetromino2(r, c):
    """
    ㅗ 모양 테트로미노
    """
    global answer

    wings = []

    for dr, dc in d:
        nr, nc = r + dr, c + dc

        if 0 <= nr < N and 0 <= nc < M:
            wings.append(paper[nr][nc])

    if len(wings) >= 3:
        answer = max(
            answer, paper[r][c] + sum(wings) - (0 if len(wings) == 3 else min(wings))
        )


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        tetromino1(i, j, 1, paper[i][j])
        visited[i][j] = False
        tetromino2(i, j)

print(answer)
