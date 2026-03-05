# 나머지도 분배법칙 성립 -> (A-B) % C = (A%C - B%C) % C
# 나머지가 나누어 떨어지려면 -> A%C == B%C
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

R = {}
for s in S:
    s %= M
    R[s] = R.get(s, 0) + 1

answer = 0
for n in R.values():
    if n > 1:  # rC2
        answer += n * (n - 1) // 2
print(answer)
