class Solution {
public:
    vector<vector<int>> answer;

    void bt_swap(vector<int>& nums, int start) {
        if (start == nums.size()) {
            answer.push_back(nums);
            return;
        }

        for (int i = start; i < nums.size(); i++) {
            swap(nums[start], nums[i]);
            bt_swap(nums, start + 1);
            swap(nums[start], nums[i]);
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        bt_swap(nums, 0);
        return answer;
    }
};
