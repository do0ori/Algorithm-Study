class Solution {
public:
    vector<string> answer;

    void bt(int n, string group, int open, int close) {
        if (open == n && close == n) {
            answer.push_back(group);
            return;
        }

        if (open < n) {
            bt(n, group + "(", open + 1, close);
        }

        if (close < n && open > close) {
            bt(n, group + ")", open, close + 1);
        }
    }

    vector<string> generateParenthesis(int n) {
        bt(n, "", 0, 0);
        return answer;
    }
};
