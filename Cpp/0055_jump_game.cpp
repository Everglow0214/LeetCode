// https://leetcode.cn/problems/jump-game/

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_reach = 0;
        for (int i = 0; i < nums.size(); ++i) {
            max_reach = max(max_reach, i + nums[i]);
            if ((i == max_reach) && (max_reach < nums.size()-1)) {
                return false;
            }
        }
        return true;
    }
};

