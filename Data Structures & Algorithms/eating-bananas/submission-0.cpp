class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // k와 h가 반비례 FFF[T]TT
        int l = 1, r = *max_element(piles.begin(), piles.end());
        while (l <= r) {
            int m = int((l + r) / 2);
            int cnt = 0;
            for (int pile : piles) {
                cnt += pile / m;
                if (pile % m) cnt++;
            }

            if (cnt > h) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return l;
    }
};
