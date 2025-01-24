# 최소 신장 트리
import heapq as hq

def is_connected(graph, start, goal):
    visited = set()
    stack = [start]
    
    while stack:
        n = stack.pop()
        
        if n == goal:
            return True
        
        if n not in visited:
            visited.add(n)
            stack.extend(graph[n])
        
    return False

def solution(n, costs):
    # cost 작은 순서로 정렬
    heap = []
    for n1, n2, cost in costs:
        hq.heappush(heap, [cost, n1, n2])

    graph = {i: [] for i in range(n)}
    min_cost = 0
    cnt = 0
    # n-1개의 다리를 건설하면 모두 이어짐
    while cnt != n - 1:
        cost, n1, n2 = hq.heappop(heap)    # 가장 작은 cost를 가지는 다리 가져오기
        
        if not is_connected(graph, n1, n2):
            graph[n1].append(n2)
            graph[n2].append(n1)
            min_cost += cost
            cnt += 1
    
    return min_cost