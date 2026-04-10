def solution(n, times):
    answer = 0
    t_low, t_high = 1, max(times) * n   # 최소 심사 시간, 최대 심사 시간
    
    while t_low <= t_high:
        mid = (t_high + t_low) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break
        if people >= n:
            answer = mid
            t_high = mid - 1
        else:
            t_low = mid + 1
            
    return answer