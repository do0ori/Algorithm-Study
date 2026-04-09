#include <bits/stdc++.h>

using namespace std;

/*
 *  n-1의 우측에 2x1 추가 (1가지 방법) -> dp[n-1] * 1
 *  n-2의 우측에 1x2, 2x2 추가 (2가지 방법) -> dp[n-2] * 2
 *      => dp[n] = dp[n-1] + dp[n-2] * 2
 */
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    if (N == 1) {
        cout << 1;
    } else if (N == 2) {
        cout << 3;
    } else {
        vector<int> dp(N + 1);
        dp[1] = 1;
        dp[2] = 3;
        for (int i = 3; i < N + 1; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007;
        }
        cout << dp[N];
    }

    return 0;
}