#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string line) {
    string answer = "";
    char prev = '\0';

    for (char c : line) {
        if (prev != c) {
            answer += c;
            prev = c;
        } else if (answer.back() != '*') {
            answer += '*';
        }
    }

    return answer;
}

void test(const string& input, const string& expected) {
    string actual = solution(input);
    if (actual == expected) {
        cout << "[PASS] " << input << '\n';
    } else {
        cout << "[FAIL] " << input
             << " | expected: " << expected
             << " | actual: " << actual << '\n';
    }
}

int main() {
    std::vector<std::pair<std::string, std::string>> cases = {
        {"aabbbc", "a*b*c"},
        {"helllllllo", "hel*o"},
        {"wonderful", "wonderful"},
        // 추가 테스트
        {"a", "a"},
        {"aa", "a*"},
        {"ab", "ab"},
        {"aabb", "a*b*"},
        {"aaab", "a*b"},
        {"abb", "ab*"},
        {"zzz", "z*"}
    };

    for (const auto& case_pair : cases) {
        test(case_pair.first, case_pair.second);
    }
}