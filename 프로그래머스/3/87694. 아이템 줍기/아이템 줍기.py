"""
- 51x51에 0 1 로 사각형을 채워서 표시
    - 테두리가 아닌 곳은 상하좌우가 모두 1
    - character는 무조건 테두리에서 시작 -> item에 도달할 때까지 이웃한 점으로 이동 -> item에 도달했을 때 반환되는 이동 거리가 최소 거리 (BFS)
- 경로를 건너뛰는 문제 => 좌표를 두 배로 하고 결과 값은 2로 나누기
"""
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 모든 좌표를 2배로 늘려서 1단위로 이동했을 때 빈틈이 생기지 않도록 함
    MAX_COORD = 102 # 범위 체크 안해도 됨
    board = [[0] * MAX_COORD for _ in range(MAX_COORD)]
    
    # 1. 직사각형의 테두리를 표시
    # 내부를 먼저 채우고, 테두리를 덮어쓰는 방식으로 구현
    for lx, ly, rx, ry in rectangle:
        # 좌표를 2배로 늘림
        lx, ly, rx, ry = lx * 2, ly * 2, rx * 2, ry * 2
        
        # 내부를 1로 채움
        for x in range(lx, rx + 1):
            for y in range(ly, ry + 1):
                board[x][y] = 1

    # 2. 겹치는 부분과 내부를 0으로 표시
    for lx, ly, rx, ry in rectangle:
        # 좌표를 2배로 늘림
        lx, ly, rx, ry = lx * 2, ly * 2, rx * 2, ry * 2

        # 테두리를 제외한 내부를 0으로 만듦
        # x좌표는 lx+1부터 rx-1까지, y좌표는 ly+1부터 ry-1까지
        for x in range(lx + 1, rx):
            for y in range(ly + 1, ry):
                board[x][y] = 0

    # BFS를 위한 큐와 방문 배열
    q = deque()
    q.append((characterX * 2, characterY * 2, 0)) # (x, y, 거리)
    visited = [[False] * MAX_COORD for _ in range(MAX_COORD)]
    visited[characterX * 2][characterY * 2] = True
    
    # 3. BFS 실행
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        cx, cy, dist = q.popleft()
        
        # 아이템 위치에 도달하면 거리 반환
        if cx == itemX * 2 and cy == itemY * 2:
            return dist // 2  # 2배로 늘린 좌표계이므로 실제 거리는 절반

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            # 테두리 & 방문하지 않은 경우
            if board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))