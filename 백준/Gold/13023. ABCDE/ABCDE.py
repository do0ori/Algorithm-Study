# 친구 관계가 연속으로 5명 이어지는 경우가 있는지 보는 문제

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * N


def dfs(start, depth):
    if depth == 4:
        return True
    visited[start] = True
    for friend in graph[start]:
        if not visited[friend]:
            if dfs(friend, depth + 1):
                return True
    visited[start] = False
    return False


for i in range(N):
    if dfs(i, 0):
        print(1)
        break
else:
    print(0)
