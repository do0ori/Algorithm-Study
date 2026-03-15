import sys

input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    i = 1
    while data[i] != -1:
        next_node = data[i]
        weight = data[i + 1]
        graph[node].append((next_node, weight))
        i += 2


def dfs(start):
    stack = [(start, 0)]
    visited = [False] * (V + 1)
    visited[start] = True

    far_node = start
    far_dist = 0

    while stack:
        now, dist = stack.pop()

        if dist > far_dist:
            far_dist = dist
            far_node = now

        for nxt, cost in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append((nxt, dist + cost))

    return far_node, far_dist


# 1번 정점에서 가장 먼 정점 찾기
far_node, _ = dfs(1)

# 그 정점에서 가장 먼 거리 = 트리의 지름
_, answer = dfs(far_node)

print(answer)
