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
    return answer[0] == '0' ? "0" : answer;
}