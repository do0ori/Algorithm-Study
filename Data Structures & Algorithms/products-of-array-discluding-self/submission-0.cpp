class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix;
        vector<int> suffix;
        int pp = 1;
        int sp = 1;
        for (int i = 0; i < nums.size(); i++) {
            pp *= nums[i];
            sp *= nums[nums.size() - 1 - i];
            prefix.push_back(pp);
            suffix.push_back(sp);
        }
        
        vector<int> answer;
        int left, right;
        for (int i = 0; i < nums.size(); i++) {
            left = i > 0 ? prefix[i - 1] : 1;
            right = i < nums.size() - 1 ? suffix[nums.size() - 2 - i] : 1;
            answer.push_back(left * right);
        }

        return answer;
    }
};
