#include <bits/stdc++.h>
using namespace std;

vector<int> dr = {0, 0, 1, -1};
vector<int> dc = {1, -1, 0, 0};

int solution(int N, int M, vector<vector<int>> board) {
    vector<vector<bool>> visited(N, vector<bool>(M, false));
    int group = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (board[i][j] == 1 && !visited[i][j]) {
                visited[i][j] = true;
                stack<pair<int, int>> st;
                st.push({i, j});
                while (!st.empty()) {
                    auto [r, c] = st.top();
                    st.pop();

                    for (int idx = 0; idx < 4; idx++) {
                        int nr = r + dr[idx];
                        int nc = c + dc[idx];

                        if (0 <= nr && nr < N && 0 <= nc && nc < M &&
                            board[nr][nc] == 1 && !visited[nr][nc]) {
                            visited[nr][nc] = true;
                            st.push({nr, nc});
                        }
                    }
                }
                group++;
            }
        }
    }
    return group;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        int M, N, K;
        cin >> M >> N >> K;

        // board[row][col] = board[y][x]
        vector<vector<int>> board(N, vector<int>(M, 0));

        for (int i = 0; i < K; i++) {
            int x, y;
            cin >> x >> y;
            board[y][x] = 1;
        }

        cout << solution(N, M, board) << '\n';
    }

    return 0;
}