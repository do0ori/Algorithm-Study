from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pizzas = deque(
        [
            {"number": i + 1, "cheese": cheese}
            for i, cheese in enumerate(map(int, input().split()))
        ]
    )
    oven = deque([pizzas.popleft() for _ in range(N)])
    table = []

    while len(table) != M:
        for i in range(N):
            pizza = oven[i]
            if pizza["cheese"] == 0:
                table.append(pizza["number"])
                if pizzas:
                    next_pizza = pizzas.popleft()
                    next_pizza["cheese"] //= 2
                    oven[i] = next_pizza
                else:
                    oven[i] = {"cheese": -1}
            else:
                pizza["cheese"] //= 2
                oven[i] = pizza

    print(f"#{test_case} {table[-1]}")
