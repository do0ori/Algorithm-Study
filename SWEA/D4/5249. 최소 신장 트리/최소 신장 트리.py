def isConnected(graph, s, g):
    visited = set()
    stack = [s]

    while stack:
        node = stack.pop()

        if node == g:
            return True

        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

    return False


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = {v: [] for v in range(V + 1)}
    weight = {}
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
        weight[(n1, n2)] = w

    sorted_weight = sorted(weight.items(), key=lambda x: x[1], reverse=True)

    selected_graph = {v: [] for v in range(V + 1)}
    selected_edge = []
    edge_cost = 0

    # N개의 노드를 가진 트리에서 N-1개의 간선을 선택하면 모두 연결됨
    while len(selected_edge) < V:
        (n1, n2), min_weight = sorted_weight.pop()
        if not isConnected(selected_graph, n1, n2):
            selected_graph[n1].append(n2)
            selected_graph[n2].append(n1)
            selected_edge.append((n1, n2))
            edge_cost += min_weight

    print(f"#{test_case} {edge_cost}")
