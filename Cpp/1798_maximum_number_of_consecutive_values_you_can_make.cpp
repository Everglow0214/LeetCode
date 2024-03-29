// https://leetcode.cn/problems/maximum-number-of-consecutive-values-you-can-make/

class Solution {
public:
    int getMaximumConsecutive(vector<int>& coins) {
        sort(coins.begin(), coins.end());
        int res = 1;
        for (int coin: coins) {
            if (coin > res) {
                break;
            }
            res += coin;
        }
        return res;
    }
};
