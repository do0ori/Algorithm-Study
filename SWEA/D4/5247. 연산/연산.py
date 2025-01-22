from collections import deque


def isValid(x, visited):
    return 0 < x <= 1000000 and not visited[x]  # 범위 제한 및 방문 여부 확인


def bfs_step(n, m):
    visited = [0 for _ in range(1000001)]  # 중복 계산 방지
    queue = deque([n])
    step = 0

    while queue:
        for _ in range(len(queue)):
            num = queue.popleft()

            if num == m:
                return step

            for cal_result in [num + 1, num - 1, num * 2, num - 10]:
                if isValid(cal_result, visited):
                    visited[cal_result] = 1
                    queue.append(cal_result)

        step += 1


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    print(f"#{test_case} {bfs_step(N, M)}")
