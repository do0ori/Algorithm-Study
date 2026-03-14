N, M = map(int, input().split())

maze = [list(input()) for i in range(N)]
visit = [[0]*M for j in range(N)]
queue = [(0,0)]

while(queue):
    x, y = queue.pop(0)
        
    if x-1 >= 0 and visit[x-1][y] == 0 and maze[x-1][y] == '1':
        queue.append((x-1,y))
        visit[x-1][y] = visit[x][y] + 1
    if x+1 < N and visit[x+1][y] == 0 and maze[x+1][y] == '1':
        queue.append((x+1,y))
        visit[x+1][y] = visit[x][y] + 1
    if y-1 >= 0 and visit[x][y-1] == 0 and maze[x][y-1] == '1':
        queue.append((x,y-1))
        visit[x][y-1] = visit[x][y] + 1
    if y+1 < M and visit[x][y+1] == 0 and maze[x][y+1] == '1':
        queue.append((x,y+1))
        visit[x][y+1] = visit[x][y] + 1

print(visit[N-1][M-1] + 1)