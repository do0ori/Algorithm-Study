import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
chon1, chon2 = map(int, input().split())
M = int(input())
family = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

visited = [False] * (N + 1)


def bfs(start, end):
    chon = 0
    visited[start] = True
    q = deque([start])

    while q:
        for _ in range(len(q)):
            p = q.popleft()
            if p == end:
                return chon

            for adj in family[p]:
                if not visited[adj]:
                    visited[adj] = True
                    q.append(adj)
        chon += 1

    return -1


print(bfs(chon1, chon2))
