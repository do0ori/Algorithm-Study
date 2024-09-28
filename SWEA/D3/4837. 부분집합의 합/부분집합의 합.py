from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    subset_N = combinations([i for i in range(1, 13)], N)
    answer = sum([sum(subset) == K for subset in subset_N])
    print(f"#{test_case} {answer}")
