"""
w:  1, 3, 5
t:       3, 8

w:  2,                    11, 12, 13,  18
t:    3, 4, 5, 7, 7, 9, 9,           17, 20, 20

w:      5, 6,    10, 11, 11, 13, 14, 14,                      19, 20
t:  1, 4, 5, 8, 9,             13,     15, 16, 17, 17, 18, 18
"""

from bisect import bisect_left

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    w_list = sorted(map(int, input().split()))
    t_list = sorted(map(int, input().split()))

    total_w = 0
    num_used_t = 0
    for w in w_list[::-1]:
        num_available_t = M - bisect_left(t_list, w) - num_used_t
        if num_available_t:
            total_w += w
            num_used_t += 1

    print(f"#{test_case} {total_w}")
