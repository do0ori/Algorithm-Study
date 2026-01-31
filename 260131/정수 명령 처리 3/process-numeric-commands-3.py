n = int(input())
cmd = []
num = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] in ["push_front", "push_back"]:
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
from collections import deque

q = deque()
for c, n in zip(cmd, num):
    if c == "push_front":
        q.append(n)
    elif  c == "push_back":
        q.appendleft(n)
    elif c == "pop_front":
        print(q.pop())
    elif c == "pop_back":
        print(q.popleft())
    elif c == "size":
        print(len(q))
    elif c == "empty":
        print(1 if not q else 0)
    elif c == "front":
        print(q[-1])
    elif c == "back":
        print(q[0])