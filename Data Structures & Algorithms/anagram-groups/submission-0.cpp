#include <array>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int, 26>, vector<string>> group;
        for (string& str : strs) {
            array<int, 26> alphabet{};
            for (char c : str) {
                alphabet[c - 'a']++;
            }
            group[alphabet].push_back(str);
        }

        vector<vector<string>> answer;
        for (auto& p : group) {
            answer.push_back(p.second);
        }

        return answer;
    }
};
