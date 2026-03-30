class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (auto& num : nums) {
            count[num]++;
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>> max_heap;
        for (auto& p : count) {
            max_heap.push({p.second, p.first});
        }

        vector<int> answer;
        for (int i = 0; i < k; i++) {
            answer.push_back(max_heap.top().second);
            max_heap.pop();
        }

        return answer;
    }
};
