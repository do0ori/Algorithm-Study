import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
computers = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

infected = set([1])


def dfs(computer):
    for adj in computers[computer]:
        if adj not in infected:
            infected.add(adj)
            dfs(adj)


dfs(1)
print(len(infected) - 1)
