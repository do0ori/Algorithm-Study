class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> cars;
        for (int i = 0; i < position.size(); i++) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.begin(), cars.end());

        stack<double> st;

        for (int i = (int)cars.size() - 1; i >= 0; i--) {
            double arrival_time = cal_time(target, cars[i]);

            if (st.empty() || st.top() < arrival_time) {
                st.push(arrival_time);
            }
        }

        return st.size();
    }

    double cal_time(int distance, pair<int, int> car) {
        return (double)(distance - car.first) / car.second;
    }
};