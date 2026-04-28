class Solution {
public:
    vector<vector<int>> answer;

    void dfs(int i, vector<int>& comb, int total, vector<int>& nums, int target) {
        if (total > target) return;

        if (total == target) {
            answer.push_back(comb);
            return;
        }

        for (int nxt = i; nxt < nums.size(); nxt++) {
            comb.push_back(nums[nxt]);
            dfs(nxt, comb, total + nums[nxt], nums, target);
            comb.pop_back();
        }
    }

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> combination;
        dfs(0, combination, 0, nums, target);
        return answer;
    }
};
