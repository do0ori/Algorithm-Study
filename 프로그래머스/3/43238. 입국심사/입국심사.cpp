#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, vector<int> times) {
    long long l = 1;
    long long r = 1LL * (*max_element(times.begin(), times.end())) * n;
    
    while (l <= r) {
        long long m = (l + r) / 2;
        
        long long people = 0;
        for (int time : times) {
            people += m / time;
            if (people >= n) break;
        }
        
        if (people >= n) {
            r = m - 1;
        } else {
            l = m + 1;
        }
    }
    return l;
}