class Solution {
public:
    vector<vector<int>> answer;
    vector<int> subset;

    void dfs(vector<int>& nums, int start) {
        answer.push_back(subset);

        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i - 1]) continue;

            subset.push_back(nums[i]);
            dfs(nums, i + 1);
            subset.pop_back();
        }
    }

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        dfs(nums, 0);
        return answer;
    }
};