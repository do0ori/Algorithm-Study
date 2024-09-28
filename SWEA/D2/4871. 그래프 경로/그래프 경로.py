def dfs_path_checker(graph, start, goal):
    visited = set()  # 방문한 노드
    stack = [start]  # 탐색할 노드

    while stack:
        node = stack.pop()
        if node == goal:
            return 1

        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])  # 인접한 노드 추가

    return 0


T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    graph = {i: [] for i in range(1, V + 1)}  # 노드를 미리 모두 빈 리스트로 초기화
    for _ in range(E):
        node_from, node_to = map(int, input().split())
        graph[node_from].append(node_to)

    S, G = map(int, input().split())

    print(f"#{test_case} {dfs_path_checker(graph, S, G)}")
