import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(N)]

answer = float("inf")

for shelters in combinations(points, K):
    max_dist = 0

    for pr, pc in points:
        nearest = float("inf")

        for sr, sc in shelters:
            nearest = min(nearest, abs(sr - pr) + abs(sc - pc))

        max_dist = max(max_dist, nearest)

    answer = min(answer, max_dist)

print(answer)
