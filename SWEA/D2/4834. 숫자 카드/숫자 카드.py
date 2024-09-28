T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cards = input()
    card_count_dict = {}
    # 카드 빈도 수 세기 (카드 번호: 횟수)
    for card in cards:
        card_count_dict[card] = card_count_dict.get(card, 0) + 1
    # 횟수 -> 카드 번호 기준으로 오름차순 정렬
    sorted_cards = sorted(card_count_dict.items(), key=lambda x: (x[1], x[0]))
    card, card_count = sorted_cards[-1]  # 가장 큰 값 가져오기
    print(f"#{test_case} {card} {card_count}")
