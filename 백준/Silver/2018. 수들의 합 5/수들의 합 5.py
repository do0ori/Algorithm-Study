# 투 포인터
N = int(input())
start = end = 1
answer = 1  # 자기자신
total = 1
while end != N:
    if total == N:
        answer += 1
        end += 1
        total += end
    elif total > N:
        total -= start
        start += 1
    else:
        end += 1
        total += end
print(answer)
