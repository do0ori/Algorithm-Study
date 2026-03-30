class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> ppair = {
            {')', '('},
            {'}', '{'},
            {']', '['},
        };
        for (auto& p : s) {
            if (ppair.contains(p)) {
                if (st.empty() || st.top() != ppair[p]) return false;
                st.pop();
            } else {
                st.push(p);
            }
        }
        return st.empty();
    }
};
