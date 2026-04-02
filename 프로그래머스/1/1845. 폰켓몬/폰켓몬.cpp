#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> nums)
{
    set<int> s;
    for (int num : nums) {
        s.insert(num);
    }
    
    return min(s.size(), nums.size() / 2);
}