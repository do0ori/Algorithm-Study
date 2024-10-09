def dfs_min(bus_stop, total, min_total):
    if min_total <= total:  # 가지치기
        return min_total

    if bus_stop == N:  # 종료 조건
        return min(min_total, total)

    for step in range(1, battery[bus_stop - 1] + 1):
        next_bus_stop = bus_stop + step
        if next_bus_stop <= N:
            min_total = dfs_min(
                next_bus_stop, total if next_bus_stop == N else total + 1, min_total
            )  # 도착 정류장에는 배터리가 없으므로 total 그대로 전달

    return min_total


T = int(input())
for test_case in range(1, T + 1):
    N, *battery = map(int, input().split())

    min_battery_change = dfs_min(1, 0, N)

    print(f"#{test_case} {min_battery_change}")
