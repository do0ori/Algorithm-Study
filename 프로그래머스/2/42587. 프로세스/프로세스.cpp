#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> priorities, int location) { 
    queue<pair<int, int>> q;
    for (int i = 0; i < priorities.size(); i++) {
        q.push({priorities[i], i});
    }
    
    sort(priorities.begin(), priorities.end(), greater<int>());
    
    int idx = 0;
    int answer = 0;
    while (!q.empty()) {
        auto curr = q.front();
        q.pop();
        
        if (priorities[idx] == curr.first) {
            answer++;
            idx++;
            
            if (curr.second == location) return answer;
        } else {
            q.push(curr);
        }
    }
    
    return answer;
}