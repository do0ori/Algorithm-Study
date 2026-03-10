import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)


def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        for adj in graph[node]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)


answer = 0
for i in range(1, N + 1):
    if not visited[i]:
        answer += 1
        dfs(i)

print(answer)
