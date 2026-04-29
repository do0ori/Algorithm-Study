class Solution {
public:
    vector<vector<int>> answer;

    void bt_bit_mask(vector<int>& nums, vector<int> perms, int mask) {
        if (perms.size() == nums.size()) {
            answer.push_back(perms);
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (!(mask & 1 << i)) {
                perms.push_back(nums[i]);
                bt_bit_mask(nums, perms, mask | 1 << i);
                perms.pop_back();
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        bt_bit_mask(nums, {}, 0);
        return answer;
    }
};
