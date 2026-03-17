import sys

input = sys.stdin.readline

N = int(input())
k = int(input())

left, right = 1, k
while left <= right:
    mid = (left + right) // 2
    # 현재 숫자(mid) 이하인 원소 개수
    cnt = sum([min(mid // i, N) for i in range(1, N + 1)])
    if cnt >= k:
        right = mid - 1
    else:
        left = mid + 1

print(left)
