class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<pair<int, int>> st;   // {start index, height}
        int n = heights.size();
        int lra = 0;

        for (int i = 0; i < n; i++) {
            int h = heights[i];
            int si = i;
            while(!st.empty() && st.top().second > h) {
                auto [start_index, height] = st.top();
                st.pop();

                lra = max(lra, (i - start_index) * height);
                si = start_index;
            }
            st.push({si, h});
        }

        while (!st.empty()) {
            auto [start_index, height] = st.top();
            st.pop();

            lra = max(lra, (n - start_index) * height);
        }

        return lra;
    }
};
