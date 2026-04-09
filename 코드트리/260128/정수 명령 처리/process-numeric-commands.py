N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))
    else:
        value.append(0)

# Please write your code here.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
    
    def pop(self):
        print(self.stack.pop())
    
    def size(self):
        print(len(self.stack))
    
    def empty(self):
        print(1 if not self.stack else 0)
    
    def top(self):
        print(self.stack[-1])
    

s = Stack()
for c, v in zip(command, value):
    if c == "push":
        s.push(v)
    elif c == "pop":
        s.pop()
    elif c == "size":
        s.size()
    elif c == "empty":
        s.empty()
    else:
        s.top()