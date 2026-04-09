#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string word1, word2;
    unordered_map<char, int> alphabet;

    cin >> word1;
    for (char c : word1) {
        alphabet[c]++;
    }

    cin >> word2;
    for (char c : word2) {
        alphabet[c]--;
    }

    int answer = 0;
    for (const auto &[k, v] : alphabet) {
        answer += abs(v);
    }

    cout << answer;

    return 0;
}