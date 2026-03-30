class Solution {
public:
    int maxArea(vector<int>& heights) {
        int answer = 0;
        int l = 0, r = heights.size() - 1;
        while (l < r) {
            int area = (r - l) * min(heights[l], heights[r]);
            answer = max(answer, area);
            if (heights[l] <= heights[r]) {
                l++;
            } else {
                r--;
            }
        }

        return answer;
    }
};
