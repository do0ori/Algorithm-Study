#include <string>
#include <vector>
#include <queue>

using namespace std;

void bfs(int c, vector<vector<int>>& computers, int* visited) {
    queue<int> q;
    q.push(c);
    
    while (!q.empty()) {
        int computer = q.front();
        q.pop();
        
        for (int i = 0; i < computers.size(); i++) {
            if (visited[i] == 0 && computers[computer][i] == 1) {
                visited[i] = 1;
                q.push(i);
            }
        }
    }
}

int solution_bfs(int n, vector<vector<int>> computers) {
    int cnt = 0;
    int visited[200] = {0,};
    for (int i = 0; i < n; i++) {
        if (visited[i] == 0) {
            visited[i] = 1;
            bfs(i, computers, visited);
            cnt++;
        }
    }
    
    return cnt;
}

void dfs(int c, vector<vector<int>>& computers, int* visited) {
    visited[c] = 1;

    for (int i = 0; i < computers.size(); i++) {
        if (visited[i] == 0 && computers[c][i] == 1) {
            dfs(i, computers, visited);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {
    int cnt = 0;
    int visited[200] = {0,};
    for (int i = 0; i < n; i++) {
        if (visited[i] == 0) {
            dfs(i, computers, visited);
            cnt++;
        }
    }
    
    return cnt;
}