def dfs(graph, visited, start):
    stack = graph[start]

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            stack.extend(graph[node])


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    forms = list(map(int, input().split()))
    graph = {n: [] for n in range(1, N + 1)}
    for i in range(M):
        m1, m2 = forms[i * 2], forms[i * 2 + 1]
        graph[m1].append(m2)
        graph[m2].append(m1)

    visited = [False] * (N + 1)
    cnt = 0

    for i in range(1, N + 1):
        if visited[i]:
            continue
        dfs(graph, visited, i)
        cnt += 1

    print(f"#{test_case} {cnt}")
