import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    H, L = map(int, input().split())
    belt = [list(map(int, input().split())) for _ in range(H)]

    C = {}  # 번호: 위치(h, l) 저장
    for h in range(H):
        for l in range(L):
            if belt[h][l] != -1:
                C[belt[h][l]] = (h, l)

    time = 0
    curr_b = [0] * H  # 층별 컨베이어 벨트 위치
    for i in range(1, len(C) + 1):
        h, l = C[i]

        dist_b = abs(curr_b[h] - l)
        time += h * 20 + min(dist_b, L - dist_b) * 5

        curr_b[h] = l

    print(time)
