from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for departure, arrival in tickets:
        graph[departure].append(arrival)
    
    all_paths = []

    def dfs(current, path):
        if len(path) == len(tickets) + 1:
            all_paths.append(path)
            return
        
        for i, next_dest in enumerate(graph[current]):
            graph[current].pop(i)
            dfs(next_dest, path + [next_dest])
            graph[current].insert(i, next_dest)
    
    dfs("ICN", ["ICN"])

    return sorted(all_paths)[0]
