#include <bits/stdc++.h>
using namespace std;

static vector<int> build_spf(int n) {
    vector<int> spf(n + 1);
    for (int i = 0; i <= n; i++)
        spf[i] = i;
    for (int i = 2; 1LL * i * i <= n; i++) {
        if (spf[i] != i)
            continue;
        for (int j = i * i; j <= n; j += i) {
            if (spf[j] == j)
                spf[j] = i;
        }
    }
    return spf;
}

static vector<int> transform_arr(const vector<int> &arr,
                                 const vector<int> &spf) {
    int len = (int)arr.size();
    if (len == 1)
        return arr;

    int p = spf[len];
    vector<vector<int>> buckets(p);
    for (int i = 0; i < len; i++)
        buckets[i % p].push_back(arr[i]);

    vector<int> result;
    result.reserve(len);
    for (int i = 0; i < p; i++) {
        vector<int> part = transform_arr(buckets[i], spf);
        result.insert(result.end(), part.begin(), part.end());
    }
    return result;
}

vector<int> solution(int n) {
    vector<int> arr(n);
    iota(arr.begin(), arr.end(), 1);
    vector<int> spf = build_spf(n);
    return transform_arr(arr, spf);
}

static void print_vec(const vector<int> &v) {
    cout << '[';
    for (int i = 0; i < (int)v.size(); i++) {
        if (i)
            cout << ',';
        cout << v[i];
    }
    cout << ']';
}

void run_test(int tc, int n, vector<int> expected) {
    vector<int> actual = solution(n);
    if (actual == expected)
        cout << "[PASS] problem3 test #" << tc << '\n';
    else {
        cout << "[FAIL] problem3 test #" << tc << "\n  expected=";
        print_vec(expected);
        cout << "\n  actual=";
        print_vec(actual);
        cout << '\n';
    }
}

int main() {
    run_test(1, 2, {1, 2});
    run_test(2, 4, {1, 3, 2, 4});
    run_test(3, 8, {1, 5, 3, 7, 2, 6, 4, 8});
    run_test(4, 9, {1, 4, 7, 2, 5, 8, 3, 6, 9});
    return 0;
}
