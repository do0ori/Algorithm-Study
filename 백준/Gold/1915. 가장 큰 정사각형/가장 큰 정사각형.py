# 가장 큰 정사각형의 한 변의 길이 구하기
# D[i][j]: (i, j 위치에서 왼쪽 위로 만들 수 있는 최대 정사각형 변 길이 저장)
#   => D[i][j] = min(D[i - 1][j], D[i - 1][j - 1], D[i][j - 1]) + 1
import sys

input = sys.stdin.readline

D = [[0 for j in range(1001)] for i in range(1001)]
N, M = map(int, input().split())
max = 0

for i in range(0, N):
    numbers = list(input())
    for j in range(0, M):
        D[i][j] = int(numbers[j])
        if D[i][j] == 1 and j > 0 and i > 0:
            D[i][j] = min(D[i - 1][j - 1], D[i - 1][j], D[i][j - 1]) + D[i][j]
        if max < D[i][j]:
            max = D[i][j]

print(max * max)
