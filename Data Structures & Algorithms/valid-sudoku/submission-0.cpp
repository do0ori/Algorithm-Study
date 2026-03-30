class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // check row
        for (int row = 0; row < 9; row++) {
            unordered_set<char> unique;
            for (int col = 0; col < 9; col++) {
                if (board[row][col] == '.') continue;
                if (unique.contains(board[row][col])) return false;
                unique.insert(board[row][col]);
            }
        }

        // check col
        for (int col = 0; col < 9; col++) {
            unordered_set<char> unique;
            for (int row = 0; row < 9; row++) {
                if (board[row][col] == '.') continue;
                if (unique.contains(board[row][col])) return false;
                unique.insert(board[row][col]);
            }
        }

        // check sub-box
        for (int square = 0; square < 9; square++) {
            unordered_set<char> unique;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;
                    if (board[row][col] == '.') continue;
                    if (unique.contains(board[row][col])) return false;
                    unique.insert(board[row][col]);
                }
            }
        }

        return true;
    }
};
