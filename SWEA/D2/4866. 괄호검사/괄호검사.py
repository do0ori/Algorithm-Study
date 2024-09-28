def checker(text):
    pair = {"}": "{", ")": "("}
    stack = []
    for t in text:
        if t in pair.values():
            stack.append(t)
        elif t in pair:
            if not stack or stack.pop() != pair[t]:
                return 0
    return 0 if stack else 1


T = int(input())
for test_case in range(1, T + 1):
    text = input()
    print(f"#{test_case} {checker(text)}")
