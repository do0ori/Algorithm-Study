import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    start = tuple(map(int, input().split()))
    store = {tuple(map(int, input().split())): False for _ in range(N)}
    i, j = tuple(map(int, input().split()))
    stack = [start]

    while stack:
        cx, cy = stack.pop()
        if abs(cx - i) + abs(cy - j) <= 1000:
            print("happy")
            break

        for s in store:
            x, y = s
            if abs(cx - x) + abs(cy - y) <= 1000 and not store[s]:
                store[s] = True
                stack.append(s)
    else:
        print("sad")
