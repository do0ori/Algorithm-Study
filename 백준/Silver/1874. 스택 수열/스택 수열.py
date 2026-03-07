n = int(input())
target = [int(input()) for _ in range(n)]
stack = []
num = 1
op = []
for t in target:
    while num <= t:
        stack.append(num)
        op.append("+")
        num += 1
    if stack[-1] != t:
        print("NO")
        break
    stack.pop()
    op.append("-")
else:
    for o in op:
        print(o)
