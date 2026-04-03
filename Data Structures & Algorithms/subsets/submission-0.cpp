class Solution {
public:
    vector<vector<int>> answer;

    void bt(const vector<int>& nums, vector<int>& subset, int i = 0) {
        if (i == nums.size()) {
            answer.push_back(subset);
            return;
        }

        bt(nums, subset, i + 1);

        subset.push_back(nums[i]);
        bt(nums, subset, i + 1);
        subset.pop_back();
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> subset;
        bt(nums, subset);

        return answer;
    }
};
