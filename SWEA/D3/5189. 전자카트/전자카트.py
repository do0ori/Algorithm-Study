from itertools import permutations

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    consumption = [list(map(int, input().split())) for _ in range(N)]

    min_battery = 100 * N
    for path in permutations(range(2, N + 1)):
        path = [1] + list(path) + [1]
        battery = 0
        for i in range(len(path) - 1):
            battery += consumption[path[i] - 1][path[i + 1] - 1]
        min_battery = min(min_battery, battery)

    print(f"#{test_case} {min_battery}")
