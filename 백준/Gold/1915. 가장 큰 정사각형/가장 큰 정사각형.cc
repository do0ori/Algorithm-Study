#include <bits/stdc++.h>

using namespace std;

/*
 *  가장 큰 정사각형의 한 변의 길이 구하기
 *  `D[i][j]` : (i, j) 위치에서 왼쪽 위로 만들 수 있는 최대 정사각형 변 길이
 *  => `D[i][j] = min(D[i - 1][j], D[i - 1][j - 1], D[i][j - 1]) + 1`
 */
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    vector<vector<int>> D(N, vector<int>(M, 0));
    int side = 0;

    for (int i = 0; i < N; i++) {
        string row;
        cin >> row;
        for (int j = 0; j < M; j++) {
            if (row[j] == '1') {
                D[i][j] = 1;

                if (i > 0 && j > 0) {
                    D[i][j] =
                        min({D[i - 1][j], D[i - 1][j - 1], D[i][j - 1]}) + 1;
                }
            }

            side = max(side, D[i][j]);
        }
    }

    cout << side * side;
    return 0;
}