// https://leetcode.cn/problems/integer-break/

class Solution {
public:
    int integerBreak(int n) {
        if (n < 4) {
            return n-1;
        }

        vector<int> dp(n+1, 1);
        dp[3] = 2;
        for (int i = 4; i <= n; ++i) {
            dp[i] = max(max(2*(i-2), 2*dp[i-2]), max(3*(i-3), 3*dp[i-3]));
        }
        return dp[n];
    }
};
