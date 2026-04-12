#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board) {
    int answer = 0;
    int n = board.size(), m = board[0].size();
    vector<int> dr = {-1, 1, 0, 0, -1, -1, 1, 1};
    vector<int> dc = {0, 0, -1, 1, -1, 1, -1, 1};
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < m; c++) {
            if (board[r][c] == 1) continue;
            
            bool is_dangerous = false;
            for (int i = 0; i < 8; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (0 <= nr && nr < n && 0 <= nc && nc < m) {
                    if (board[nr][nc] == 1) {
                        is_dangerous = true;
                        break;
                    }
                }
            }
            if (!is_dangerous) answer++;
        }   
    }
    return answer;
}