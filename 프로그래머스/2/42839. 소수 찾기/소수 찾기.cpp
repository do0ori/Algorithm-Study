#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

bool is_prime(int number) {
    if (number < 2) return false;
    for (int i = 2; i * i <= number; i++) {
        if (number % i == 0) return false;
    }
    return true;
}

void dfs(string& numbers, vector<bool>& visited, string cur, unordered_set<int>& made) {
    if (!cur.empty()) {
        made.insert(stoi(cur));
    }
    
    for (int i = 0; i < numbers.size(); i++) {
        if (visited[i]) continue;
        
        visited[i] = true;
        dfs(numbers, visited, cur + numbers[i], made);
        visited[i] = false;
    }
}

int solution(string numbers) {
    unordered_set<int> made;
    vector<bool> visited(numbers.size(), false);
    
    dfs(numbers, visited, "", made);
    
    int answer = 0;
    for (int num : made) {
        if (is_prime(num)) answer++;
    }
    return answer;
}