import heapq as hq


def solution(operations):
    min_heap = []
    max_heap = []
    visited = {}   # 삭제 동기화용 딕셔너리
    
    def sync_min():
        while min_heap and visited[min_heap[0]] == 0:
            hq.heappop(min_heap)
    
    def sync_max():
        while max_heap and visited[-max_heap[0]] == 0:
            hq.heappop(max_heap)
    
    for op in operations:
        command, number = op.split()
        number = int(number)
        
        if command == 'I':
            hq.heappush(min_heap, number)
            hq.heappush(max_heap, -number)
            visited[number] = visited.get(number, 0) + 1
        elif command == 'D':
            if number == 1 and max_heap:
                sync_max()
                if max_heap:
                    visited[-hq.heappop(max_heap)] -= 1
            elif number == -1 and min_heap:
                sync_min()
                if min_heap:
                    visited[hq.heappop(min_heap)] -= 1
    
    sync_min()
    sync_max()

    return [-max_heap[0], min_heap[0]] if min_heap and max_heap else [0, 0]