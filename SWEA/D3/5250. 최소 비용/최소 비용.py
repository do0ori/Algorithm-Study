import heapq


# https://namu.wiki/w/다익스트라%20알고리즘
def dijkstra():
    while heap:
        cost, (r, c) = heapq.heappop(heap)  # 최소 cost를 가지는 노드 선택

        if (r, c) == (N - 1, N - 1):  # 오른쪽 아래 도달
            return cost

        if not visited[r][c]:
            # 모든 이웃 노드들에 대해 더 작은 cost 값으로 갱신
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    if d[nr][nc] > d[r][c] + 1 + max(graph[nr][nc] - graph[r][c], 0):
                        d[nr][nc] = d[r][c] + 1 + max(graph[nr][nc] - graph[r][c], 0)
                        heapq.heappush(heap, (d[nr][nc], (nr, nc)))

            visited[r][c] = True


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    d = [[float("inf")] * N for _ in range(N)]
    d[0][0] = 0
    heap = [(0, (0, 0))]  # (cost, (r, c))
    print(f"#{test_case} {dijkstra()}")


"""
제한 시간 초과
"""

# def dfs_min(position, total, min_total):
#     if min_total <= total:  # 가지치기
#         return min_total

#     if position == (N - 1, N - 1):  # 종료조건 = 오른쪽 아래 도달
#         return min(min_total, total)

#     for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#         r, c = position
#         nr, nc = r + dr, c + dc

#         if 0 <= nr < N and 0 <= nc < N:
#             height_diff = max(graph[nr][nc] - graph[r][c], 0)
#             min_total = dfs_min((nr, nc), total + 1 + height_diff, min_total)

#     return min_total


# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     graph = [list(map(int, input().split())) for _ in range(N)]
#     print(f"#{test_case} {dfs_min((0, 0), 0, float('inf'))}")
