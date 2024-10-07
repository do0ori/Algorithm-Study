# python deque는 내부적으로 doubly linked list로 구현되어 있다.
from collections import deque


T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    numbers = deque(map(int, input().split()))

    i = 0
    for _ in range(K):
        new_i = i + M
        i = new_i % len(numbers) if new_i != len(numbers) else new_i
        prev, later = numbers[i - 1], numbers[i] if i != len(numbers) else numbers[0]
        numbers.insert(i, prev + later)

    password = []
    for _ in range(len(numbers) if len(numbers) <= 10 else 10):
        password.append(str(numbers.pop()))

    print(f"#{test_case} {' '.join(password)}")
