"""
N = 10 => f1 = 1
N = 20 => f2 =  3
N = 30 => f3 = 2 * f1 + f2 = 5

f(n) = 2 * f(n-2) + f(n-1)
"""

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    n = N // 10 - 1

    f = [1, 3]
    for i in range(2, n + 1):
        f.append(2 * f[i - 2] + f[i - 1])

    print(f"#{test_case} {f[n]}")
