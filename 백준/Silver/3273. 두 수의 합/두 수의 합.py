N = int(input())
arr = set(map(int, input().split()))
X = int(input())

answer = 0
for i in range(1, (X + 1) // 2):
    if i in arr and (X - i) in arr:
        answer += 1

print(answer)
