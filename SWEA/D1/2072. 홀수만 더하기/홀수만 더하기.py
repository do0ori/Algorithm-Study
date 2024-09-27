T = int(input())
for test_case in range(1, T + 1):
    numbers = map(int, input().split())
    print(f'#{test_case} {sum(filter(lambda x: bool(x % 2), numbers))}')