#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int, vector<int>, greater<int>> min_heap(scoville.begin(), scoville.end());
    int answer = 0;
    while (min_heap.top() < K) {
        if (min_heap.size() < 2) return -1;
        
        int s1 = min_heap.top(); min_heap.pop();
        int s2 = min_heap.top(); min_heap.pop();
        min_heap.push(s1 + s2 * 2);
        answer++;
    }
    return answer;
}