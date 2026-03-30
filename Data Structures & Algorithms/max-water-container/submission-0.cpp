class Solution {
public:
    int maxArea(vector<int>& heights) {
        int answer = 0;
        int l = 0, r = heights.size() - 1;
        while (l < r) {
            answer = (r - l) * min(heights[l], heights[r]);
            if (heights[l] < heights[r] && heights[l] < heights[l + 1]) {
                l++;
            } else if ((heights[l] > heights[r] && heights[r] < heights[r - 1])) {
                r--;
            } else {
                if (heights[l] < heights[l + 1]) {
                    l++;
                } else if (heights[r] < heights[r - 1]) {
                    r--;
                } else {
                    break;
                }
            }
        }

        return answer;
    }
};
