import sys
from collections import deque

input = sys.stdin.readline
MAX = 100001

N, K = map(int, input().split())


def bfs():
    visited = [0] * MAX
    visited[N] = 1
    q = deque([N])

    while q:
        for _ in range(len(q)):
            x = q.popleft()

            if x == K:
                return visited[x] - 1

            for nx in [x - 1, x + 1, x * 2]:
                if 0 <= nx < MAX and not visited[nx]:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
    return -1


print(bfs())
