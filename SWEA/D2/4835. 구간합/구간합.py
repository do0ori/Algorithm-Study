T = int(input())
for test_case in range(1, T + 1):
    M_sum = []
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    for i in range(0, N - M + 1):
        M_sum.append(sum(numbers[i : i + M]))
    print(f"#{test_case} {max(M_sum) - min(M_sum)}")
