T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    sale_prices = list(map(int, input().split()))

    max_profit = 0
    max_price = 0
    for sale_price in sale_prices[::-1]:
        if max_price < sale_price:
            max_price = sale_price
        else:
            max_profit += max_price - sale_price

    print(f"#{test_case} {max_profit}")
