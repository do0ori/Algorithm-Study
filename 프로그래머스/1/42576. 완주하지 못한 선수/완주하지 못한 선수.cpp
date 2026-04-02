#include <bits/stdc++.h>

using namespace std;

// 동명이인 가능
string solution(vector<string> participant, vector<string> completion) {
    unordered_map<string, int> cnt;
    for (string p : participant) {
        cnt[p]++;
    }
    
    for (string c : completion) {
        cnt[c]--;
    }
    
    for (const auto& [k, v] : cnt) {
        if (v) return k;
    }
}