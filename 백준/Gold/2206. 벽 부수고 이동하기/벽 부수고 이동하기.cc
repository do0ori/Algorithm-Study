#include <bits/stdc++.h>
using namespace std;

struct Data {
    int r;
    int c;
    int broken;
    int dist;
};

int solution(int N, int M, vector<vector<int>> board) {
    queue<Data> q;
    q.push({0, 0, 0, 1});

    vector<vector<vector<int>>> visited(
        N, vector<vector<int>>(M, vector<int>(2, false)));
    visited[0][0][0] = true;

    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};
    while (!q.empty()) {
        Data d = q.front();
        q.pop();

        if (d.r == N - 1 && d.c == M - 1) {
            return d.dist;
        }

        for (int i = 0; i < 4; i++) {
            int nr = d.r + dr[i];
            int nc = d.c + dc[i];

            if (0 <= nr && nr < N && 0 <= nc && nc < M) {
                // 다음 칸이 길인 경우
                if (board[nr][nc] == 0 && !visited[nr][nc][d.broken]) {
                    visited[nr][nc][d.broken] = true;
                    q.push({nr, nc, d.broken, d.dist + 1});

                    // 다음 칸이 벽이고, 아직 안 부쉈다면
                } else if (board[nr][nc] == 1 && d.broken == 0 &&
                           !visited[nr][nc][1]) {
                    visited[nr][nc][1] = true;
                    q.push({nr, nc, 1, d.dist + 1});
                }
            }
        }
    }

    return -1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    vector<vector<int>> board(N, vector<int>(M));

    for (int i = 0; i < N; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < M; j++) {
            board[i][j] = row[j] - '0';
        }
    }

    cout << solution(N, M, board) << '\n';
    return 0;
}