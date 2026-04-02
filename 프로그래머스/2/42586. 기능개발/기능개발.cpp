#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> days_left;
    for (int i = 0; i < progresses.size(); i++) {
        days_left.push(ceil((double)(100 - progresses[i]) / speeds[i]));
    }
    
    while (!days_left.empty()) {
        int cnt = 0;
        int deploy = days_left.front();
        while (!days_left.empty() && days_left.front() <= deploy) {
            days_left.pop();
            cnt++;
        }
        answer.push_back(cnt);
    }
    
    return answer;
}