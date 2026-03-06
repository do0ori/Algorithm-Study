import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
A.sort()
answer = 0

for i, target in enumerate(A):
    left, right = 0, N - 1

    while left < right:
        total = A[left] + A[right]

        if total == target:
            if left != i and right != i:
                answer += 1
                break
            elif left == i:
                left += 1
            elif right == i:
                right -= 1
        elif total > target:
            right -= 1
        else:
            left += 1

print(answer)
