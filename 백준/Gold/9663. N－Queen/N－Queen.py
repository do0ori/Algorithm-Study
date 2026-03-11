# 퀸은 가로, 세로, 대각선으로
"""
대각선 계산 어떻게?
(r, c index 범위: 0 ~ N-1)
    /는 r+c 값 동일
        index 범위: 0 ~ 2N-2
        배열 크기 = 2N-2 - 0 + 1 = 2N-1
    \는 r-c 값 동일
        index 범위: -(N-1) ~ N-1
        배열 크기 = N-1 - (-(N-1)) + 1 = 2N-1
        => 음수 index 보정해주려면 r-c + (N-1)로 계산
"""

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())

cols = [False] * N
diag1 = [False] * (2 * N - 1)  # /
diag2 = [False] * (2 * N - 1)  # \
answer = 0


def bt(r=0):
    global answer

    if r == N:
        answer += 1
        return

    for c in range(N):
        if not cols[c] and not diag1[r + c] and not diag2[r - c + N - 1]:
            cols[c] = diag1[r + c] = diag2[r - c + N - 1] = True
            bt(r + 1)
            cols[c] = diag1[r + c] = diag2[r - c + N - 1] = False


bt()
print(answer)
