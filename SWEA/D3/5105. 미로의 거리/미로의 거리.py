from collections import deque


def bfs_find_min_path(start, goal, maze):
    visited = [[False] * N for _ in range(N)]
    queue = deque([start])
    step = 0

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            if [r, c] == goal:
                return step - 1  # 0만 step에 포함

            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < N
                    and 0 <= nc < N
                    and maze[nr][nc] != 1
                    and not visited[nr][nc]
                ):
                    queue.append([nr, nc])
                    visited[nr][nc] = True

        step += 1

    return 0  # goal에 도착하지 못하고 while문이 종료됨


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                start = [r, c]
            elif maze[r][c] == 3:
                goal = [r, c]

    print(f"#{test_case} {bfs_find_min_path(start, goal, maze)}")
