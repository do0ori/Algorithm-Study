import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
chon1, chon2 = map(int, input().split())
M = int(input())
family = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)


def bfs(start, end):
    visited = [0] * (N + 1)
    visited[start] = 1
    q = deque([start])

    while q:
        for _ in range(len(q)):
            c = q.popleft()
            if c == end:
                return visited[c] - 1

            for adj in family[c]:
                if not visited[adj]:
                    visited[adj] = visited[c] + 1
                    q.append(adj)

    return -1


print(bfs(chon1, chon2))
