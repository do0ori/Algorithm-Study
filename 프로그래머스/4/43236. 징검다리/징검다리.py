def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    
    left = 0
    right = distance    # 거리의 최솟값의 최댓값
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        removed_rock = 0
        prev_rock = 0
        min_d = 1000000001
        
        for rock in rocks:
            if rock - prev_rock < mid:
                removed_rock += 1
            else:
                min_d = min(min_d, rock - prev_rock)
                prev_rock = rock
        
        if removed_rock > n:
            right = mid - 1
        else:
            answer = min_d
            left = mid + 1
    
    return answer