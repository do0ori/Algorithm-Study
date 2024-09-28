T = int(input())
for test_case in range(1, T + 1):
    text = input()

    prev_text = None
    stack = list(text)
    while prev_text != stack:
        prev_text = stack
        stack = []
        for t in prev_text:
            if stack and stack[-1] == t:
                stack.pop()
            else:
                stack.append(t)

    print(f"#{test_case} {len(stack)}")
