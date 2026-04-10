#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    vector<int> time(N + 1);
    vector<int> indegree(N + 1);      // prev 개수
    vector<vector<int>> graph(N + 1); // prev: [post]
    vector<int> dp(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> time[i];
        int j;
        while (cin >> j) {
            if (j == -1)
                break;
            indegree[i]++;
            graph[j].push_back(i);
        }
    }

    queue<int> q;
    for (int i = 1; i <= N; i++) {
        if (indegree[i] == 0) {
            dp[i] = time[i];
            q.push(i);
        }
    }

    while (!q.empty()) {
        int curr = q.front();
        q.pop();

        for (int nxt : graph[curr]) {
            dp[nxt] = max(dp[nxt], dp[curr] + time[nxt]);
            indegree[nxt]--;
            if (indegree[nxt] == 0)
                q.push(nxt);
        }
    }

    for (int i = 1; i <= N; i++) {
        cout << dp[i] << '\n';
    }

    return 0;
}