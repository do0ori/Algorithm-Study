#include <string>
#include <vector>

using namespace std;

string solution(vector<int> numbers, string hand) {
    int left = 9, right = 11;
    char press = '\0';
    string answer = "";
    for (int number : numbers) {
        number--;
        switch (number) {
            case 0:
            case 3:
            case 6:
                press = 'L'; break;
            case 2:
            case 5:
            case 8:
                press = 'R'; break;
            case 1:
            case 4:
            case 7:
            case -1:
                if (number == -1) number = 10;
                
                int l_dist = abs(left / 3 - number / 3) + abs(left % 3 - number % 3);
                int r_dist = abs(right / 3 - number / 3) + abs(right % 3 - number % 3);
                if (l_dist == r_dist) {
                    press = hand == "right" ? 'R' : 'L';
                } else if (l_dist < r_dist) {
                    press = 'L';
                } else {
                    press = 'R';
                }
                break;
        }
        
        if (press == 'L') {
            left = number;
        } else {
            right = number;
        }
        answer += press;
    }
    return answer;
}