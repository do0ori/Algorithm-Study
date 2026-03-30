class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (auto& num : nums) {
            count[num]++;
        }

        vector<int> answer;
        for (auto& p : count) {
            if (p.second >= k ) {
                answer.push_back(p.first);
            }
        }

        return answer;
    }
};
