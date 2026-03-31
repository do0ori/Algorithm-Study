#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

string solution(string s) {
    vector<int> v;
    stringstream ss(s);
    int x;
    while(ss >> x) v.push_back(x);
    sort(v.begin(), v.end());
    return to_string(v.front()) + " " + to_string(v.back());
}