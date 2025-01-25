from collections import defaultdict, deque


def solution(n, edge):
    graph = defaultdict(list)
    
    for n1, n2 in edge:
        graph[n1].append(n2)
        graph[n2].append(n1)

    answer = 0
    queue = deque([1])
    visit = [False] * (n + 1)
    visit[1] = True
    
    while queue:
        answer = len(queue)
        
        for _ in range(len(queue)):
            node = queue.popleft()
            
            for adj in graph[node]:
                if not visit[adj]:
                    visit[adj] = True
                    queue.append(adj)
    
    return answer