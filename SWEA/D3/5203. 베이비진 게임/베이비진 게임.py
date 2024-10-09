def is_baby_gin(cards):
    if 3 in cards:  # triplet
        return True

    for j in range(10 - 2):  # run
        if all(cards[j : j + 3]):
            return True

    return False


T = int(input())
for test_case in range(1, T + 1):
    cards = map(int, input().split())

    result = 0
    cards1 = [0] * 10
    cards2 = [0] * 10
    for i, card in enumerate(cards):
        cards, player = (cards1, 1) if (i + 1) % 2 == 1 else (cards2, 2)
        cards[card] += 1

        if is_baby_gin(cards):
            result = player
            break

    print(f"#{test_case} {result}")
