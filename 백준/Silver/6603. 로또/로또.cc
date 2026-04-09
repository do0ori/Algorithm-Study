#include <bits/stdc++.h>

using namespace std;

int K;

void dfs(int start, vector<int> &list, const vector<int> S) {
    if (list.size() == 6) {
        for (int l : list) {
            cout << l << ' ';
        }
        cout << '\n';
        return;
    }

    for (int i = start; i < K; i++) {
        list.push_back(S[i]);
        dfs(i + 1, list, S);
        list.pop_back();
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    while (true) {
        cin >> K;
        if (K == 0)
            break;

        vector<int> S(K);
        for (int i = 0; i < K; i++) {
            cin >> S[i];
        }

        vector<int> numbers;
        dfs(0, numbers, S);
        cout << '\n';
    }

    return 0;
}