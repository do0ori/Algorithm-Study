import sys
from collections import deque

input = sys.stdin.readline
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)


def dfs_recursive(node):
    print(node, end=" ")
    visited[node] = True

    for adj in graph[node]:
        if not visited[adj]:
            dfs_recursive(adj)


def dfs_iterative(start):
    visited = [False] * (N + 1)
    stack = [start]

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            print(node, end=" ")

        for adj in reversed(graph[node]):
            if not visited[adj]:
                stack.append(adj)


def bfs(start):
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque([start])

    while q:
        node = q.popleft()
        print(node, end=" ")
        for adj in graph[node]:
            if not visited[adj]:
                visited[adj] = True
                q.append(adj)


dfs_recursive(V)
print()

# dfs_iterative(V)
# print()

bfs(V)
print()
