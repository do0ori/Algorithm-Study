n = int(input())

# Please write your code here.
from collections import deque

q = deque(range(1, n+1))
while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])