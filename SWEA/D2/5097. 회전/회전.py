T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    print(f"#{test_case} {numbers[M % N]}")
