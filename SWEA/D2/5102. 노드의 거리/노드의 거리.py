from collections import deque


def bfs_graph_min_path(graph, start_node, goal_node):
    visited = set([start_node])
    queue = deque([start_node])
    count = 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            if node == goal_node:
                return count

            for route in graph[node]:
                if route not in visited:
                    visited.add(route)
                    queue.append(route)

        count += 1

    return 0  # goal_node에 도착하지 못하고 while문이 종료됨


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = {v + 1: [] for v in range(V)}
    for e in range(E):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
    S, G = map(int, input().split())

    print(f"#{test_case} {bfs_graph_min_path(graph, S, G)}")
