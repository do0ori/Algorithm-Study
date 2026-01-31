N = int(input())
command = []
A = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        A.append(int(line[1]))
    else:
        A.append(0)

# Please write your code here.
from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, num):
        self.dq.append(num)
    
    def pop(self):
        print(self.dq.pop())
    
    def size(self):
        print(len(self.dq))
    
    def empty(self):
        print(1 if not self.dq else 0)
    
    def front(self):
        print(self.dq[0])

q = Queue()
for c, a in zip(command, A):
    if c == "push":
        q.push(a)
    elif c == "pop":
        q.pop()
    elif c == "size":
        q.size()
    elif c == "empty":
        q.empty()
    else:
        q.front()