def binary_search_cnt(size, target):
    start = 1
    end = size
    cnt = 0
    while start <= end:
        cnt += 1
        mid = (start + end) // 2
        if mid == target:
            return cnt
        elif mid < target:
            start = mid
        else:
            end = mid
    return cnt


T = int(input())  # 테스트 케이스의 수 입력
for test_case in range(1, T + 1):
    P, P_a, P_b = map(
        int, input().split()
    )  # 전체 페이지, A가 찾는 페이지, B가 찾는 페이지

    N_a = binary_search_cnt(P, P_a)  # A의 탐색 횟수
    N_b = binary_search_cnt(P, P_b)  # B의 탐색 횟수

    # 결과 판단
    if N_a == N_b:
        result = 0  # 비긴 경우
    elif N_a < N_b:
        result = "A"  # A가 이긴 경우
    else:
        result = "B"  # B가 이긴 경우

    print(f"#{test_case} {result}")
