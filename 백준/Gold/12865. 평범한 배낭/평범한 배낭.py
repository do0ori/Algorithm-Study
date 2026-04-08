"""
물건을 넣는다 / 안 넣는다
dp[j] = 무게 한도가 j일 때 최대 가치

`0/1 배낭`이라서 뒤에서부터 1차원 DP 갱신
    앞에서 돌면 dp[j - w]가 이미 현재 물건을 반영한 값일 수 있어.
    그러면 현재 물건을 또 넣게 돼서
    같은 물건을 여러 번 사용하는 효과가 생김.

    뒤에서 돌면 dp[j - w]는 아직 이전 물건들만 반영된 값이야.
    그래서 현재 물건을 지금 딱 한 번만 추가하는 형태가 됨.

점화식: dp[j] = max(dp[j], dp[j-w] + v)
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (K + 1)

for _ in range(N):
    w, v = map(int, input().split())
    for j in range(K, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[K])
