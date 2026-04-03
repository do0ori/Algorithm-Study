#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> priorities, int location) { 
    queue<pair<int, int>> q;
    for (int i = 0; i < priorities.size(); i++) {
        q.push({priorities[i], i});
    }
    
    int answer = 0;
    while (!q.empty()) {
        auto curr = q.front();
        q.pop();
        
        bool is_highest = true;
        for (int i = 0; i < q.size(); i++) {
            auto wait = q.front();
            q.pop(); q.push(wait);
            if (wait.first > curr.first) is_highest = false;
        }
        
        if (is_highest) {
            answer++;
            if (curr.second == location) return answer;
        } else {
            q.push(curr);
        }
    }
}