#include <bits/stdc++.h>
using namespace std;

vector<int> dr = {0, 0, 1, -1};
vector<int> dc = {1, -1, 0, 0};

int solution(int N, int M, vector<vector<int>> board) {
    queue<pair<int, int>> q;
    int unripe = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (board[i][j] == 1) {
                q.push({i, j});
            } else if (board[i][j] == 0) {
                unripe++;
            }
        }
    }
    int r, c;
    while (!q.empty()) {
        auto pos = q.front();
        r = pos.first;
        c = pos.second;
        q.pop();

        for (int idx = 0; idx < 4; idx++) {
            int nr = r + dr[idx];
            int nc = c + dc[idx];

            if (0 <= nr && nr < N && 0 <= nc && nc < M && board[nr][nc] == 0) {
                board[nr][nc] = board[r][c] + 1;
                q.push({nr, nc});
                unripe--;
            }
        }
    }

    return unripe > 0 ? -1 : board[r][c] - 1;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N;
    cin >> M >> N;

    // board[row][col]
    vector<vector<int>> board(N, vector<int>(M));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> board[i][j];
        }
    }

    cout << solution(N, M, board) << '\n';
    return 0;
}