#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<vector<int>> board(rows, vector<int>(columns));
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            board[i][j] = i * columns + j + 1;
        }
    }
    
    vector<int> answer;
    for (auto query : queries) {
        int x1 = query[0] - 1, y1 = query[1] - 1;
        int x2 = query[2] - 1, y2 = query[3] - 1;
        int prev = board[x1][y1];
        int min_n = prev;
        // right
        for (int y = y1 + 1; y <= y2; y++) {
            swap(prev, board[x1][y]);
            min_n = min(min_n, prev);
        }
        // down
        for (int x = x1 + 1; x <= x2; x++) {
            swap(prev, board[x][y2]);
            min_n = min(min_n, prev);
        }
        // left
        for (int y = y2 - 1; y >= y1; y--) {
            swap(prev, board[x2][y]);
            min_n = min(min_n, prev);
        }
        // up
        for (int x = x2 - 1; x >= x1; x--) {
            swap(prev, board[x][y1]);
            min_n = min(min_n, prev);
        }
        answer.push_back(min_n);
    }
    return answer;
}