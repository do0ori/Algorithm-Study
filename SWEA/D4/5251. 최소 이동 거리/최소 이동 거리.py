import heapq


def dijkstra():
    while heap:
        d, n = heapq.heappop(heap)  # 최소 거리 노드 가져오기

        if n == N:
            return d

        if not visited[n]:
            for adj_n in graph[n]:
                if not weight[(n, adj_n)]:
                    continue
                if distance[adj_n] > distance[n] + weight[(n, adj_n)]:
                    distance[adj_n] = distance[n] + weight[(n, adj_n)]
                    heapq.heappush(heap, (distance[adj_n], adj_n))

            visited[n] = True


T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int, input().split())
    graph = {n: [] for n in range(N + 1)}
    weight = {}
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append(e)
        weight[(s, e)] = w
    distance = [float("inf")] * (N + 1)
    distance[0] = 0
    visited = [False] * (N + 1)
    heap = [(0, 0)]  # (distance, node)
    print(f"#{test_case} {dijkstra()}")
