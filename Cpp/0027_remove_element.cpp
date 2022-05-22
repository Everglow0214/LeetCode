// https://leetcode.cn/problems/remove-element/

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n = nums.size();
        int i = 0, j = n-1;

        while (i <= j) {
            if (nums[i] == val) {
                nums[i] = nums[j];
                j = j - 1;
            }
            else {
                i = i + 1;
            }
        }

        return i;
    }
};