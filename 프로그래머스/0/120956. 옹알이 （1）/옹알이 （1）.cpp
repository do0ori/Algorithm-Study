#include <string>
#include <vector>

using namespace std;

int solution(vector<string> babbling) {
    int answer = 0;
    vector<string> words = {"aya", "ye", "woo", "ma"};

    for (const string& s : babbling) {
        int i = 0;

        while (i < s.size()) {
            bool matched = false;

            for (const string& w : words) {
                if (i + w.size() <= s.size() && s.substr(i, w.size()) == w) {
                    i += w.size();
                    matched = true;
                    break;
                }
            }

            if (!matched) break;
        }

        if (i == s.size()) answer++;
    }

    return answer;
}