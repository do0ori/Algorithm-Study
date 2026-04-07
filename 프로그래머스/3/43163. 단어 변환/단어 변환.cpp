#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using namespace std;

bool is_convertable(string word1, string word2) {
    int cnt = 0;
    for (int i = 0; i < word1.size(); i++) {
        if (word1[i] != word2[i]) {
            if (cnt == 1) return false;
            cnt++;
        }
    }
    return true;
}

int solution(string begin, string target, vector<string> words) {
    if (find(words.begin(), words.end(), target) == words.end()) return 0;
    
    unordered_map<string, vector<string>> graph;
    words.push_back(begin);
    for (string word1 : words) {
        for (string word2 : words){
            if (is_convertable(word1, word2)) {
                graph[word1].push_back(word2);
                graph[word2].push_back(word1);
            }
        }
    }
    
    queue<string> q;
    q.push(begin);
    unordered_set<string> visited;
    visited.insert(begin);
    int answer = 0;
    
    while (!q.empty()) {
        int qs = q.size();
        for (int i = 0; i < qs; i++) {
            string word = q.front();
            q.pop();
            
            if (word == target) {
                return answer;
            }
            
            for (string nxt : graph[word]) {
                if (visited.find(nxt) == visited.end()) {
                    visited.insert(nxt);
                    q.push(nxt);
                }                
            }
        }
        answer++;
    }

    return 0;
}