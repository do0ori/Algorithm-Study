#include <bits/stdc++.h>
using namespace std;

string solution(vector<int> numbers) {
    vector<string> strs;
    for (int x : numbers) {
        strs.push_back(to_string(x));
    }

    sort(strs.begin(), strs.end(), [](const string& a, const string& b) {
        return a + b > b + a;
    });

    string answer = "";
    for (const string& s : strs) {
        answer += s;
    }

    // 모든 숫자가 0인 경우 0 하나만 반환해야 함
    return answer[0] == '0' ? "0" : answer;
}