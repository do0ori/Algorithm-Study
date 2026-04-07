#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, K;
    vector<vector<int>> medals;

    cin >> N >> K;
    
    int nation, gold, silver, copper;
    vector<int> target;
    for (int i = 0; i < N; i++) {
        cin >> nation >> gold >> silver >> copper;
        medals.push_back({gold, silver, copper});
        if (nation == K) {
            target = {gold, silver, copper};
        }
    }

    int rank = 1;
    for (auto medal : medals) {
        if (medal > target) {
            rank++;
        }
    }
    
    cout << rank;
    
    return 0;
}