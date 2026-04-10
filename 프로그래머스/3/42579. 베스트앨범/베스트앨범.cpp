#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    unordered_map<string, priority_queue<vector<int>>> group_by_genre;
    unordered_map<string, int> genre_cnt;
    for (int i = 0; i < genres.size(); i++) {
        genre_cnt[genres[i]] += plays[i];
        group_by_genre[genres[i]].push({plays[i], -i});
    }
    
    vector<pair<string, int>> genre_cnt_sorted(genre_cnt.begin(), genre_cnt.end());
    sort(genre_cnt_sorted.begin(), genre_cnt_sorted.end(), [](const auto& a, const auto& b){
        return a.second > b.second;
    });
    
    vector<int> answer;
    for (auto [g, v] : genre_cnt_sorted) {
        auto songs = group_by_genre[g];
        for (int i = 0; i < 2; i++) {
            if (songs.empty()) break;
            answer.push_back(-songs.top()[1]);
            songs.pop();
        }
    }
    return answer;
}