from collections import deque


def solution(n, edges, ants):
    graph = [[] for _ in range(n + 1)]

    for a, b, c, d in edges:
        graph[a].append((b, c, d))
        graph[b].append((a, c, d))

    failed = []

    for ant in ants:
        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            cur = q.popleft()

            if cur == n:
                break

            for nxt, lo, hi in graph[cur]:
                if not visited[nxt] and lo <= ant <= hi:
                    visited[nxt] = True
                    q.append(nxt)
        else:
            failed.append(ant)

    if not failed:
        return [1, 1]

    return [failed[0], failed[-1]]
