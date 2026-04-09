"""
n-1의 우측에 2x1 추가 (1가지 방법) -> dp[n-1] * 1
n-2의 우측에 1x2, 2x2 추가 (2가지 방법) -> dp[n-2] * 2
    => dp[n] = dp[n-1] + dp[n-2] * 2
"""

N = int(input())

if N == 1:
    print(1)
elif N == 2:
    print(3)
else:
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007

    print(dp[N])
