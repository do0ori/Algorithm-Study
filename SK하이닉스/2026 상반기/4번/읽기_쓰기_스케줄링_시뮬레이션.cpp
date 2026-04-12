#include <bits/stdc++.h>
using namespace std;

struct Process {
    string type;
    int t1, t2, A, B;
    string C;
    int order;
};

static Process parse_process(const string &s, int order) {
    stringstream ss(s);
    Process p;
    p.order = order;
    ss >> p.type >> p.t1 >> p.t2 >> p.A >> p.B;
    if (p.type == "write")
        ss >> p.C;
    return p;
}

vector<string> solution(vector<string> arr, vector<string> processes) {
    vector<Process> ps;
    for (int i = 0; i < (int)processes.size(); i++) {
        ps.push_back(parse_process(processes[i], i));
    }

    vector<string> answers;
    queue<Process> readyReads;
    queue<Process> readyWrites;

    int idx = 0;
    int currentTime = 0;
    int activeReadFinish = -1;
    vector<pair<int, string>> activeReadOutputs;

    auto enqueue_arrivals = [&](int t) {
        while (idx < (int)ps.size() && ps[idx].t1 <= t) {
            if (ps[idx].type == "read")
                readyReads.push(ps[idx]);
            else
                readyWrites.push(ps[idx]);
            idx++;
        }
    };

    auto flush_finished_reads = [&]() {
        sort(activeReadOutputs.begin(), activeReadOutputs.end(),
             [](auto &a, auto &b) { return a.first < b.first; });
        for (auto &[ord, s] : activeReadOutputs)
            answers.push_back(s);
        activeReadOutputs.clear();
        activeReadFinish = -1;
    };

    while (idx < (int)ps.size() || !readyReads.empty() ||
           !readyWrites.empty() || activeReadFinish != -1) {
        if (activeReadFinish != -1) {
            int nextArrival = (idx < (int)ps.size() ? ps[idx].t1 : INT_MAX);
            if (nextArrival <= activeReadFinish) {
                currentTime = nextArrival;
                enqueue_arrivals(currentTime);
                continue;
            } else {
                currentTime = activeReadFinish;
                enqueue_arrivals(currentTime);
                flush_finished_reads();
                continue;
            }
        }

        if (readyWrites.empty() && readyReads.empty()) {
            currentTime = ps[idx].t1;
            enqueue_arrivals(currentTime);
        }

        if (!readyWrites.empty()) {
            Process w = readyWrites.front();
            readyWrites.pop();
            currentTime = max(currentTime, w.t1);
            for (int i = w.A - 1; i <= w.B - 1; i++)
                arr[i] = w.C;
            currentTime += w.t2;
            enqueue_arrivals(currentTime);
            continue;
        }

        if (!readyReads.empty()) {
            vector<Process> batch;
            int start = currentTime;
            while (!readyReads.empty()) {
                batch.push_back(readyReads.front());
                readyReads.pop();
            }

            int finish = start;
            for (auto &r : batch) {
                string out;
                for (int i = r.A - 1; i <= r.B - 1; i++)
                    out += arr[i];
                activeReadOutputs.push_back({r.order, out});
                finish = max(finish, start + r.t2);
            }
            activeReadFinish = finish;
            continue;
        }
    }

    answers.push_back(to_string(currentTime));
    return answers;
}

static void print_vec(const vector<string> &v) {
    cout << '[';
    for (int i = 0; i < (int)v.size(); i++) {
        if (i)
            cout << ',';
        cout << '"' << v[i] << '"';
    }
    cout << ']';
}

void run_test(int tc, vector<string> arr, vector<string> processes,
              vector<string> expected) {
    vector<string> actual = solution(arr, processes);
    if (actual == expected)
        cout << "[PASS] problem4 test #" << tc << '\n';
    else {
        cout << "[FAIL] problem4 test #" << tc << "\n  expected=";
        print_vec(expected);
        cout << "\n  actual=";
        print_vec(actual);
        cout << '\n';
    }
}

int main() {
    run_test(1, {"1", "2", "3", "4", "5"}, {"read 1 3 1 3"}, {"123", "4"});

    run_test(2, {"1", "2", "3", "4", "5"}, {"write 1 2 2 4 9", "read 4 1 1 5"},
             {"19995", "5"});

    run_test(3, {"1", "2", "3", "4", "5"},
             {"read 1 5 1 2", "write 2 3 3 5 7", "read 3 1 1 5"},
             {"12", "12777", "10"});
    return 0;
}
