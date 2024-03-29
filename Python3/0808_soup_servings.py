# https://leetcode.cn/problems/soup-servings/

class Solution:
    def soupServings(self, n):
        """
        Inputs:
            n: int
        Outputs:
            res: float
        """

        # This code is copied from other's solution.
        @cache
        def dfs(i, j):
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1
            if j <= 0:
                return 0
            return 0.25 * (dfs(i - 4, j) + dfs(i - 3, j - 1) + dfs(i - 2, j - 2) + dfs(i - 1, j - 3))
        
        return 1 if n > 4800 else dfs((n + 24) // 25, (n + 24) // 25)