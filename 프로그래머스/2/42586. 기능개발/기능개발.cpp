#include <bits/stdc++.h>

using namespace std;
/*
// queue 버전
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
*/

// queue 없는 버전
vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> days_left;
    for (int i = 0; i < progresses.size(); i++) {
        days_left.push_back(ceil((double)(100 - progresses[i]) / speeds[i]));
    }
    
    vector<int> answer;
    int cnt = 1;
    int deploy = days_left[0];
    for (int i = 1; i < days_left.size(); i++) {
        if (days_left[i] <= deploy) {
            cnt++;
        } else {
            deploy = days_left[i];
            answer.push_back(cnt);
            cnt = 1;
        }
    }
    answer.push_back(cnt);
    
    return answer;
}