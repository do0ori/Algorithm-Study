#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for (auto command : commands) {
        vector<int> sliced(array.begin() + command[0] - 1, array.begin() + command[1]);
        sort(sliced.begin(), sliced.end());
        answer.push_back(sliced[command[2] - 1]);
    }
    return answer;
}