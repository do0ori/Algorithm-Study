S, P = map(int, input().split())
source = input()
min_count = list(map(int, input().split()))

idx = {"A": 0, "C": 1, "G": 2, "T": 3}

# 초기 윈도우
window_count = [0] * 4
for s in source[0:P]:
    window_count[idx[s]] += 1

satisfied = 0
for i in range(4):
    if window_count[i] >= min_count[i]:
        satisfied += 1

answer = 1 if satisfied == 4 else 0

# 슬라이딩
for i in range(S - P):
    left, right = idx[source[i]], idx[source[i + P]]
    if window_count[left] == min_count[left]:
        satisfied -= 1
    window_count[left] -= 1

    window_count[right] += 1
    if window_count[right] == min_count[right]:
        satisfied += 1

    if satisfied == 4:
        answer += 1

print(answer)
