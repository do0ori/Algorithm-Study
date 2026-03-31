#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    char prev = ' ';    
    for (int i = 0; i < s.size(); i++) {
        if (prev == ' ') {
            s[i] = toupper(s[i]);
        } else {
            s[i] = tolower(s[i]);
        }
        prev = s[i];
    }
    return s;
}