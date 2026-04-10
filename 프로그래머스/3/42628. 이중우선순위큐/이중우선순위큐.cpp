#include <string>
#include <vector>
#include <queue>
#include <unordered_map>
#include <iostream>

using namespace std;

priority_queue<int> max_q;
priority_queue<int, vector<int>, greater<int>> min_q;
unordered_map<int, int> manage;

void sync_max() {
    while (!max_q.empty() && manage[max_q.top()] == 0) {
        max_q.pop();
    }
}

void sync_min() {
    while (!min_q.empty() && manage[min_q.top()] == 0) {
        min_q.pop();
    }
}

vector<int> solution(vector<string> operations) {
    for (string operation : operations) {
        char command = operation[0];
        int number = stoi(operation.substr(2));
        
        if (command == 'I') {
            max_q.push(number);
            min_q.push(number);
            manage[number]++;
        } else {    // 'D'
            if (number == 1) {
                sync_max();
                if (!max_q.empty()) {
                    manage[max_q.top()]--; max_q.pop();                    
                }
            } else {    // -1
                sync_min();
                if (!min_q.empty()) {
                    manage[min_q.top()]--; min_q.pop();
                }
            }
        }
    }
    
    sync_max(); sync_min();
    
    if (!max_q.empty() && !min_q.empty()) {
        return {max_q.top(), min_q.top()};
    } else {
        return {0, 0};
    }
}