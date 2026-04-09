#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, K;
    cin >> N >> K;

    vector<int> dp(K + 1); // dp[j] = 무게 한도가 j일 때 최대 가치

    for (int i = 0; i < N; i++) {
        int w, v;
        cin >> w >> v;                  // 물건 하나 선택
        for (int j = K; j > w - 1; j--) // 용량이 큰 것부터 갱신
        {
            // max(안 넣기, 넣기)
            dp[j] = max(dp[j], dp[j - w] + v);
        }
    }

    cout << dp[K];

    return 0;
}