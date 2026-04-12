#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int n, vector<vector<int>> drags) {
    vector<vector<int>> screen(n + 1);

    // 초기 상태: i번 위치에 i번 아이콘
    for (int i = 1; i <= n; i++) {
        screen[i].push_back(i);
    }

    for (const auto &drag : drags) {
        int src = drag[0];
        int dst = drag[1];

        // 아무 일도 일어나지 않는 경우
        if (src == dst)
            continue;
        if (screen[src].empty())
            continue;

        bool srcIsIcon = (screen[src].size() == 1);

        if (srcIsIcon) {
            int icon = screen[src][0];

            // 1) 아이콘 -> 빈 위치
            if (screen[dst].empty()) {
                screen[dst].push_back(icon);
                screen[src].clear();
            }
            // 2) 아이콘 -> 아이콘 위치 : 폴더 생성
            else if (screen[dst].size() == 1) {
                int other = screen[dst][0];
                screen[dst].clear();
                screen[dst].push_back(other);
                screen[dst].push_back(icon);
                screen[src].clear();
            }
            // 3) 아이콘 -> 폴더 위치 : 폴더 안에 담김
            else {
                screen[dst].push_back(icon);
                screen[src].clear();
            }
        } else {
            // src는 폴더
            // 4) 폴더 -> 빈 위치 : 이동
            // 5) 폴더 -> 아이콘/폴더 위치 : swap
            swap(screen[src], screen[dst]);
        }
    }

    // 각 아이콘의 최종 위치 복원
    vector<int> answer(n + 1);
    for (int pos = 1; pos <= n; pos++) {
        for (int icon : screen[pos]) {
            answer[icon] = pos;
        }
    }

    // 문제 형식에 맞게 1번 아이콘 ~ n번 아이콘 위치만 반환
    vector<int> result;
    result.reserve(n);
    for (int i = 1; i <= n; i++) {
        result.push_back(answer[i]);
    }
    return result;
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

static void run_test(int tc, int n, vector<vector<int>> drags,
                     vector<int> expected) {
    vector<int> actual = solution(n, drags);
    if (actual == expected) {
        cout << "[PASS] problem1 test #" << tc << '\n';
    } else {
        cout << "[FAIL] problem1 test #" << tc << "\n  expected=";
        print_vec(expected);
        cout << "\n  actual=";
        print_vec(actual);
        cout << "\n";
    }
}

int main() {
    run_test(1, 4, {{1, 2}}, {2, 2, 3, 4});
    run_test(2, 4, {{1, 2}, {3, 2}}, {2, 2, 2, 4});
    run_test(3, 4, {{1, 2}, {2, 4}}, {4, 4, 3, 2});
    run_test(4, 5, {{1, 2}, {3, 4}, {2, 4}}, {4, 4, 2, 2, 5});
    return 0;
}
