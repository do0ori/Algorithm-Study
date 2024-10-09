T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tasks = sorted(
        [list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1]
    )  # 작업 종료 시간을 기준으로 정렬

    num_task = 0
    curr_time = 0
    while curr_time < 24:
        for i, (s, e) in enumerate(tasks):
            if s >= curr_time:
                curr_time = e
                num_task += 1
                break
        else:  # 시작 가능한 작업이 없는 경우 종료
            break

    print(f"#{test_case} {num_task}")
