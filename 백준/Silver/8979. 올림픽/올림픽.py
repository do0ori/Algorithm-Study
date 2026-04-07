import sys
from collections import defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
medals = defaultdict(list)
for _ in range(N):
    nation, gold, silver, copper = map(int, input().split())
    medals[(gold, silver, copper)].append(nation)
sorted_by_medals = sorted(medals, reverse=True)

rank = 1
for medal in sorted_by_medals:
    if K in medals[medal]:
        print(rank)
        break
    rank += len(medals[medal])
