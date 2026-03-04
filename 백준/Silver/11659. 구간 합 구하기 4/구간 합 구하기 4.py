# N = M = 100000
# I = 100000000 (1초에 1억번 연산)
# 단순 방법으로는 시간 초과: N * M > I
# 구간 합: N + M < I
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + numbers[i]
for _ in range(M):
    i, j = map(int, input().split())
    print(S[j] - S[i - 1])
