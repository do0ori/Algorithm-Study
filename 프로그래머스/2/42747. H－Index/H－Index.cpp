#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> citations) {
    sort(citations.begin(), citations.end());
    for (int i = 0; i < citations.size(); i++) {
        if (citations[i] >= citations.size() - i) {
            return citations.size() - i;
        }
    }
    return 0;
}