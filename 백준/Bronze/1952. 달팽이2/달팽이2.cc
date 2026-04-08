#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int M, N;
    cin >> M >> N;

    vector<vector<bool>> visited;
    for (int i = 0; i < M; i++) {
        vector<bool> row(N, false);
        visited.push_back(row);
    }

    int dr[4] = {0, 1, 0, -1};
    int dc[4] = {1, 0, -1, 0};

    int r = 0, c = 0, d = 0;
    int answer = 0;
    
    while (true) {
        visited[r][c] = true;

        int nr = r + dr[d], nc = c + dc[d];
        if (0 <= nr && nr < M && 0 <= nc && nc < N && !visited[nr][nc]) {
            r = nr; c = nc;
        } else {
            d = (d + 1) % 4;    // 시계방향으로 90도 회전
            int nr = r + dr[d], nc = c + dc[d];
            if (0 <= nr && nr < M && 0 <= nc && nc < N && !visited[nr][nc]) {
                r = nr; c = nc;
                answer++;
            } else {
                break;
            }
        }
    }
    
    cout << answer;
    
    return 0;
}