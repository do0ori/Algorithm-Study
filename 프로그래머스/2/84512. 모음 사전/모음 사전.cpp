#include <string>
#include <vector>

using namespace std;

string vowels = "AEIOU";
int cnt = 0;
bool found = false;

void make_dict(string curr, string target) {
    if (found) return;
    if (!curr.empty()) {
        cnt++;
        if (curr == (target)) {
            found = true;
            return;
        }
    }
    
    if (curr.size() == 5) return;
    
    for (auto v : vowels) {
        make_dict(curr + v, target);
    }
}

int solution(string word) {
    make_dict("", word);
    return cnt;
}