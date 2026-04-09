#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    vector<long long> dist(N - 1);
    for (int i = 0; i < N - 1; i++) {
        cin >> dist[i];
    }

    vector<long long> cost(N);
    for (int i = 0; i < N; i++) {
        cin >> cost[i];
    }

    long long min_cost = cost[0];
    long long answer = 0;
    for (int i = 0; i < N - 1; i++) {
        min_cost = min(min_cost, cost[i]);
        answer += min_cost * dist[i];
    }

    cout << answer;

    return 0;
}