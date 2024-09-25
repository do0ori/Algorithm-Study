from collections import deque

def solution(priorities, location):
    
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    process_cnt = 0
    
    while queue:
        current = queue.popleft()
        
        if any(current[0] < item[0] for item in queue):
            queue.append(current)
        else :
            process_cnt += 1
            if current[1] == location:
                return process_cnt

    return process_cnt