n, k = map(int, input().split())

# Please write your code here.
from collections import deque

q = deque(range(n, 0, -1))
answer = []
while len(q) >= k:
    for _ in range(k-1):
        q.appendleft(q.pop())
    answer.append(q.pop())
print(' '.join(answer))