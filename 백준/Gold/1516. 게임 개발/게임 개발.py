import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
time = [0] * (N + 1)  # 1번 건물을 짓는데 걸리는 시간
graph = {i: [] for i in range(1, N + 1)}  # prev: [post]
indegree = [0] * (N + 1)  # i번 건물의 선행 건물 개수
dp = [0] * (N + 1)  # i번 건물을 짓기 위한 최소 시간
for i in range(1, N + 1):
    t, *prevs = map(int, input().split())
    prevs.pop()

    time[i] = t
    indegree[i] += len(prevs)
    for prev in prevs:
        graph[prev].append(i)

q = deque()
# 선행 건물이 없는 건물 추가
for i in range(1, N + 1):
    if indegree[i] == 0:
        dp[i] = time[i]
        q.append(i)

while q:
    curr = q.popleft()

    for nxt in graph[curr]:
        dp[nxt] = max(dp[nxt], dp[curr] + time[nxt])
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

for i in range(1, N + 1):
    print(dp[i])
