import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
d = deque(range(1, N + 1))

while len(d) != 1:
    d.popleft()
    d.append(d.popleft())

print(d[0])
