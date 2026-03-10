import sys

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
stack = []  # 인덱스를 저장
answer = [-1] * N

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)
