import heapq as hq


def solution(jobs):
    request = []
    for i, (s, l) in enumerate(jobs):
        hq.heappush(request, [s, l, i])
    
    time = 0
    priority_queue = []
    return_time = [0] * len(jobs)
    while request or priority_queue:
        # 현재 시각 전에 요청된 작업 모두 대기 큐로 가져오기
        while request and request[0][0] <= time:
            s, l, i = hq.heappop(request)
            hq.heappush(priority_queue, [l, s, i])
            
        # 없으면 가장 요청이 먼저 온 작업 대기 큐로 가져오기
        if not priority_queue and request:
            s, l, i = hq.heappop(request)
            time = s
            hq.heappush(priority_queue, [l, s, i])
            
        # 대기 큐에서 가장 우선순위가 높은 작업 수행
        l, s, i = hq.heappop(priority_queue)
        time += l
        return_time[i] = time - s
    
    return sum(return_time) // len(jobs)