import sys
from heapq import *

input = sys.stdin.readline
N = int(input())
abs_min_heap = []
for _ in range(N):
    x = int(input())
    if x != 0:
        heappush(abs_min_heap, (abs(x), x))
    else:
        if abs_min_heap:
            _, min_value = heappop(abs_min_heap)
            print(min_value)
        else:
            print(0)
