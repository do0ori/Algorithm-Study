/*
 * 1. 배열을 unordered_set으로 바꾼다.
 *      - 중복 제거
 *      - O(1)에 존재 여부 확인 가능
 * 2. 각 숫자 num에 대해:
 *      - num - 1이 없으면 시작점
 *      - 시작점이면 num+1, num+2, ... 가 있는지 계속 확인
 *      - 길이를 구해서 longest 갱신
 */

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;

        for (int num : numSet) {
            if (numSet.find(num - 1) == numSet.end()) {
                int length = 1;
                while (numSet.find(num + length) != numSet.end()) {
                    length++;
                }
                longest = max(longest, length);
            }
        }
        return longest;
    }
};
