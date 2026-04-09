#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> jobs) {
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> request;
    for (int i = 0; i < jobs.size(); i++) {
        // [요청 시각, 소요 시간, 작업 번호]
        request.push({jobs[i][0], jobs[i][1], i});
    }
    
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> min_q;
    int time = 0;
    int answer = 0;
    while (!request.empty() || !min_q.empty()) {
        // 현재 시각 전에 요청된 작업 모두 대기 큐로 가져오기
        while (!request.empty() && request.top()[0] <= time) {
            auto task = request.top(); request.pop();
            // [소요 시간, 요청 시각, 작업 번호]
            min_q.push({task[1], task[0], task[2]});
        }
        
        // 없으면 가장 요청이 먼저 온 작업 대기 큐로 가져오기
        if (min_q.empty() && !request.empty()) {
            auto task = request.top(); request.pop();
            time = task[0];
            min_q.push({task[1], task[0], task[2]});
        }
        
        // 대기 큐에서 가장 우선순위가 높은 작업 수행
        auto task = min_q.top(); min_q.pop();
        time += task[0];
        answer += time - task[1];
    }
    
    return answer / jobs.size();
}