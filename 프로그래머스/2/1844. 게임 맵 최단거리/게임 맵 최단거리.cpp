#include<vector>
#include<queue>
using namespace std;

int bfs(vector<vector<int>>& maps) {
    const int N = maps.size(), M = maps[0].size();
    queue<pair<int, int>> q;
    q.push({0, 0});
    int cnt = 1;
    maps[0][0]++;
    const vector<pair<int, int>> D = {
        {-1, 0},
        {1, 0},
        {0, -1},
        {0, 1}
    };
    
    while (!q.empty()) {
        int qs = q.size();
        for (int i = 0; i < qs; i++) {
            auto [x, y] = q.front();
            q.pop();
            
            if (x == N - 1 && y == M - 1) {
                return cnt;
            }
            
            for (auto [dx, dy] : D) {
                int nx = x + dx, ny = y + dy;
                if (0 <= nx && nx < N && 0 <= ny && ny < M && maps[nx][ny] == 1) {
                    maps[nx][ny]++;
                    q.push({nx, ny});
                }
            }
        }
        cnt++;
    }
    
    return -1;
}

int solution(vector<vector<int>> maps)
{
    return bfs(maps);
}