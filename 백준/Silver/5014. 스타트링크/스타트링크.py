import sys
from collections import deque

input = sys.stdin.readline
"""
F: 총 층 수
S: 현재 층
G: 스타링크 층(목적지)
U: 위로 이동할 수 있는 층 수
D: 아래로 이동할 수 있는 층 수
"""
F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)


def bfs(s, e):
    q = deque([s])
    visited[s] = 1

    while q:
        for _ in range(len(q)):
            x = q.popleft()  # 현재 층 수
            if x == e:  # 도착
                return visited[e] - 1

            for nx in (x + U, x - D):
                if 0 < nx <= F and not visited[nx]:
                    visited[nx] = visited[x] + 1
                    q.append(nx)

    return "use the stairs"


print(bfs(S, G))
