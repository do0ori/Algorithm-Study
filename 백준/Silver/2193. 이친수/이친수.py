# 0으로 끝나는 개수, 1로 끝나는 개수
N = int(input())
dp = [[0] * 2 for _ in range(N + 1)]
dp[1] = [0, 1]

for i in range(2, N + 1):
    dp[i][0] = sum(dp[i - 1])
    dp[i][1] = dp[i - 1][0]

print(dp[N][0] + dp[N][1])
