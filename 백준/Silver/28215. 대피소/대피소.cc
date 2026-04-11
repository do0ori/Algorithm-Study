#include <bits/stdc++.h>
using namespace std;

int manhattan(const pair<int, int> &a, const pair<int, int> &b) {
    return abs(a.first - b.first) + abs(a.second - b.second);
}

int N, K;
vector<pair<int, int>> homes;
vector<int> picked;
int answer = INT_MAX;

void evaluate() {
    int worst = 0;

    for (int i = 0; i < N; i++) {
        int best = INT_MAX;

        for (int idx : picked) {
            best = min(best, manhattan(homes[i], homes[idx]));
        }

        worst = max(worst, best);
    }

    answer = min(answer, worst);
}

void dfs(int start) {
    if ((int)picked.size() == K) {
        evaluate();
        return;
    }

    for (int i = start; i < N; i++) {
        picked.push_back(i);
        dfs(i + 1);
        picked.pop_back();
    }
}

int solution(int n, int k, const vector<pair<int, int>> &inputHomes) {
    N = n;
    K = k;
    homes = inputHomes;
    picked.clear();
    answer = INT_MAX;

    dfs(0);
    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K;
    homes.resize(N);

    for (int i = 0; i < N; i++) {
        cin >> homes[i].first >> homes[i].second;
    }

    cout << solution(N, K, homes) << '\n';
    return 0;
}