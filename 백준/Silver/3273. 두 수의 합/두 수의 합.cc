#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    unordered_set<int> arr;
    int number;
    for (int i = 0; i < N; i++) {
        cin >> number;
        arr.insert(number);
    }

    int X;
    cin >> X;

    int answer = 0;
    for (int i = 1; i < (X + 1) / 2; i++) {
        if (arr.find(i) != arr.end() && arr.find(X - i) != arr.end()) {
            answer++;
        }
    }
    cout << answer;

    return 0;
}