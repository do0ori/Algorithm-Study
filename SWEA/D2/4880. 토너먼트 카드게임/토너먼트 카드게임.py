# 1: 가위, 2: 바위, 3: 보
rps_winner = {
    (1, 1): 0,
    (1, 2): 1,
    (1, 3): 0,
    (2, 1): 0,
    (2, 2): 0,
    (2, 3): 1,
    (3, 1): 1,
    (3, 2): 0,
    (3, 3): 0,
}


# 분할 정복
def game(data, start, end):
    if start == end:
        return start

    left_winner_index = game(data, start, (start + end) // 2)
    right_winner_index = game(data, (start + end) // 2 + 1, end)
    winners_index = [left_winner_index, right_winner_index]

    result = rps_winner[(data[left_winner_index], data[right_winner_index])]
    return winners_index[result]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    winner_index = game(numbers, 0, N - 1)
    print(f"#{test_case} {winner_index + 1}")
