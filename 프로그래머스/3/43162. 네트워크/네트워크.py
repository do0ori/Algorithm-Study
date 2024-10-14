def dfs(node, computers, visited):
    visited[node] = True
    
    # 현재 노드와 연결된 모든 노드를 탐색
    for i in range(len(computers)):
        if computers[node][i] == 1 and not visited[i]:
            dfs(i, computers, visited)

def solution(n, computers):
    visited = [False] * n  # 방문 기록 배열
    network_count = 0      # 네트워크 개수
    
    # 모든 컴퓨터를 돌면서 방문하지 않은 컴퓨터 찾기
    for i in range(n):
        if not visited[i]:  # 아직 방문하지 않은 컴퓨터를 찾으면 DFS 시작
            dfs(i, computers, visited)
            network_count += 1
    
    return network_count
