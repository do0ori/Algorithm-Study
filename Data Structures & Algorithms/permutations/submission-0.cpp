class Solution {
public:
    vector<vector<int>> answer;
    
    void dfs(vector<int> nums, vector<int> perms) {
        if (nums.empty()) {
            answer.push_back(perms);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            vector<int> sub(nums.begin(), nums.begin() + i);
            sub.insert(sub.end(), nums.begin() + i + 1, nums.end());
            perms.push_back(nums[i]);
            dfs(sub, perms);
            perms.pop_back();
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        dfs(nums, {});
        return answer;
    }
};
