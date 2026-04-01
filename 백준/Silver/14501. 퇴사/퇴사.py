import sys

input = sys.stdin.readline
N = int(input())

t = [0] * N
p = [0] * N
for i in range(N):
    t[i], p[i] = map(int, input().split())

dp = [0] * (N + 1)  # i일부터 마지막 날까지 얻을 수 있는 최대 수익

for i in range(N - 1, -1, -1):
    if i + t[i] > N:  # 오늘 상담이 기간 안에 끝나지 않는 경우
        dp[i] = dp[i + 1]
    else:  # 상담 가능
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])

print(dp[0])
