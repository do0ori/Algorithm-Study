import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
targets = list(map(int, input().split()))


def binary_search(target):
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > target:
            right = mid - 1
        elif A[mid] < target:
            left = mid + 1
        else:  # mid == target
            return 1

    return 0


for target in targets:
    print(binary_search(target))
