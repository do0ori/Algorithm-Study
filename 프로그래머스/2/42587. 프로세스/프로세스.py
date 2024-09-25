from collections import deque


def solution(priorities, location):
    count = 0
    queue = deque([[p, i] for i, p in enumerate(priorities)])

    while queue:
        process = queue.popleft()
        
        # any를 사용하면 True일 경우 즉시 반환하지만 다음과 같이 max를 사용하면 항상 O(n)
        # if process[0] < max(queue, key=lambda x: x[0])[0]:
        if any(process[0] < p[0] for p in queue):
            queue.append(process)
        else:
            count += 1
            if process[1] == location:
                return count
    
    return count
