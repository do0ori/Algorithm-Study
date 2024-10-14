from collections import deque

def bfs(maps):
    n, m = len(maps), len(maps[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # BFS를 위한 큐 초기화, (row, col, 현재까지 이동한 칸의 수) 저장
    queue = deque([(0, 0, 1)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    
    while queue:
        r, c, dist = queue.popleft()
        
        if r == n - 1 and c == m - 1:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
    
    return -1   # 도착지점에 도달할 수 없는 경우

def solution(maps):
    return bfs(maps)
