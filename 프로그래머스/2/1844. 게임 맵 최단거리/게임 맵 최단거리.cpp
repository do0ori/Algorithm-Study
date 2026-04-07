#include<vector>
#include<queue>
using namespace std;

int bfs(vector<vector<int>>& maps) {
    const int N = maps.size(), M = maps[0].size();
    queue<pair<int, int>> q;
    q.push({0, 0});
    int cnt = 1;
    const vector<pair<int, int>> D = {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1}
    };
    
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();

        if (x == N - 1 && y == M - 1) {
            return maps[x][y];
        }

        for (auto [dx, dy] : D) {
            int nx = x + dx, ny = y + dy;
            if (0 <= nx && nx < N && 0 <= ny && ny < M && maps[nx][ny] == 1) {
                maps[nx][ny] = maps[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }
    
    return -1;
}

int solution(vector<vector<int>> maps)
{
    return bfs(maps);
}