class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        return set<int>(nums.begin(), nums.end()).size() != nums.size();
    }
};