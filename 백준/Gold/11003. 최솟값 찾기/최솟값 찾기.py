# 일반 정렬 O(nlogn)으로는 불가능 -> 덱 기반 정렬
from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))
d = deque()

for i in range(N):
    while d and A[d[-1]] > A[i]:
        d.pop()
    d.append(i)
    while d and i - d[0] >= L:
        d.popleft()
    print(A[d[0]], end=" ")
