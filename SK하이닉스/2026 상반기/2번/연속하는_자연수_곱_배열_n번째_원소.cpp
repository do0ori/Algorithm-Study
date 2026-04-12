#include <bits/stdc++.h>
using namespace std;

long long solution(int n) {
    static vector<long long> seq;
    if (seq.empty()) {
        const long long LIMIT = 1000000000000LL;
        for (long long a = 1; a * (a + 1) <= LIMIT; a++) {
            long long prod = a;
            for (long long b = a + 1;; b++) {
                if (prod > LIMIT / b)
                    break;
                prod *= b;
                seq.push_back(prod);
            }
        }
        sort(seq.begin(), seq.end());
        seq.erase(unique(seq.begin(), seq.end()), seq.end());
    }
    return seq[n - 1];
}

void run_test(int tc, int n, long long expected) {
    long long actual = solution(n);
    if (actual == expected)
        cout << "[PASS] problem2 test #" << tc << '\n';
    else
        cout << "[FAIL] problem2 test #" << tc << " expected=" << expected
             << " actual=" << actual << '\n';
}

int main() {
    vector<long long> first10 = {2, 6, 12, 20, 24, 30, 42, 56, 60, 72};
    for (int i = 0; i < 10; i++)
        run_test(i + 1, i + 1, first10[i]);
    return 0;
}
