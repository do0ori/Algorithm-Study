T = int(input())
for test_case in range(1, T + 1):
    step, destination, n_station = map(int, input().split())
    stations = list(map(int, input().split()))
    path = [0] * (destination + 1)
    # path에 station 위치 1로 표시
    for station in stations:
        if station > destination:
            break
        path[station] = 1

    n_charging = 0
    position = 0
    while position + step < destination:  # destination에 도착하기 전까지 계속 반복
        # 가장 가까운 충전소로 이동
        for i in range(position + step, position, -1):
            if path[i]:
                position = i
                n_charging += 1
                break
        # 가장 가까운 충전소가 없었으면 불가능
        else:
            n_charging = 0
            break
    print(f"#{test_case} {n_charging}")
