from collections import deque


def calculator(op, n1, n2):
    if op == "+":
        n = n1 + n2
    elif op == "-":
        n = n1 - n2
    elif op == "*":
        n = n1 * n2
    elif op == "/":
        n = n1 // n2
    return n


T = int(input())
for test_case in range(1, T + 1):
    expression = deque(input().split())
    operators = ["+", "-", "*", "/"]
    stack = []
    while expression:
        e = expression.popleft()
        if e in operators:
            if len(stack) < 2:
                answer = "error"
                break
            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(calculator(e, num1, num2))
        else:
            if e != ".":
                stack.append(int(e))
    else:
        if len(stack) == 1:
            answer = stack.pop()
        else:
            answer = "error"

    print(f"#{test_case} {answer}")
