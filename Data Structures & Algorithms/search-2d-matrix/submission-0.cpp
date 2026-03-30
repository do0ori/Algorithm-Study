class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int N = matrix.size();
        int M = matrix[0].size();
        int l = 0, r = N * M - 1;
        while (l <= r) {
            int m = int((l + r) / 2);
            if (matrix[int(m / M)][m % M] == target) {
                return true;
            } else if (matrix[int(m / M)][m % M] > target) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }
        return false;
    }
};
