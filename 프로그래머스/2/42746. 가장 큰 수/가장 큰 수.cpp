#include <bits/stdc++.h>

using namespace std;

string solution(vector<int> numbers) {
    sort(numbers.begin(), numbers.end(), [](int a, int b) {
        string c = to_string(a), d = to_string(b);
        return c + d > d + c;
    });
    
    string answer = "";
    for (auto n : numbers) {
        answer += to_string(n);
    }
    // 모든 숫자가 0인 경우 0 하나만 반환해야 함
    return answer[0] == '0' ? "0" : answer;
}