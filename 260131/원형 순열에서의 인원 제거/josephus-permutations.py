n, k = map(int, input().split())

# Please write your code here.
from collections import deque

q = deque(range(1, n+1))
while len(q) >= k:
    for _ in range(k-1):
        deque.appendleft(deque.pop())
    print(deque.pop())