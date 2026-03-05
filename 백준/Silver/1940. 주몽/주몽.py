# 투 포인터
N = int(input())
M = int(input())
materials = sorted(map(int, input().split()))
mat1_idx, mat2_idx = 0, N - 1
answer = 0
while mat1_idx < mat2_idx:
    total = materials[mat1_idx] + materials[mat2_idx]
    if total == M:
        answer += 1
        mat1_idx += 1
        mat2_idx -= 1
    elif total < M:
        mat1_idx += 1
    else:
        mat2_idx -= 1
print(answer)
