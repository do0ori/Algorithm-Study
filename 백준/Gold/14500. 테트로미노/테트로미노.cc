#include <bits/stdc++.h>

using namespace std;


int N, M;
int paper[500][500];
bool visited[500][500];
int answer = 0;

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

/*
 * 한 줄로 표현 가능한 테트로미노
 */
void tetromino1(int r, int c, int depth, int total) {
    if (depth == 4) {
        answer = max(answer, total);
        return;
    }

    for (int i = 0; i < 4; i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];

        if (0 <= nr && nr < N && 0 <= nc && nc < M && !visited[nr][nc]) {
            visited[nr][nc] = true;
            tetromino1(nr, nc, depth + 1, total + paper[nr][nc]);
            visited[nr][nc] = false;
        }
    }
}

/*
 * ㅗ 모양 테트로미노
 */
void tetromino2(int r, int c) {
    vector<int> wings;

    for (int i = 0; i < 4; i++) {
        int nr = r + dr[i];
        int nc = c + dc[i];

        if (0 <= nr && nr < N && 0 <= nc && nc < M ) {
            wings.push_back(paper[nr][nc]);
        }
    }

    if (wings.size() >= 3) {
        answer = max(
            answer,
            paper[r][c] +\
            accumulate(wings.begin(), wings.end(), 0) -\
            (wings.size() == 3 ? 0 : *min_element(wings.begin(), wings.end()))
        );
    }
}

int main() {
    // 빠른 입출력
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> paper[i][j];
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            visited[i][j] = true;
            tetromino1(i, j, 1, paper[i][j]);
            visited[i][j] = false;
            tetromino2(i, j);
        }
    }

    cout << answer;
    
    return 0;
}