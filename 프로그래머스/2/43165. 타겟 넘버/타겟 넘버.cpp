#include <string>
#include <vector>

using namespace std;

int dfs(int depth, int total, const int target, const vector<int>& numbers) {
    if (depth == numbers.size()) {
        return total == target ? 1 : 0;
    }
    
    return dfs(depth + 1, total + numbers[depth], target, numbers) +\
        dfs(depth + 1, total - numbers[depth], target, numbers);
}

int solution(vector<int> numbers, int target) {
    return dfs(0, 0, target, numbers);
}