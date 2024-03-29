# https://leetcode.cn/problems/find-positive-integer-solution-for-a-given-equation/

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        right_max = 1000
        for x in range(1, 1001):
            left, right = 1, right_max
            while left <= right:
                y = left + (right - left) // 2
                if customfunction.f(x, y) == z:
                    res.append([x, y])
                    right_max = y - 1
                    break
                elif customfunction.f(x, y) < z:
                    left = y + 1
                else:
                    right = y - 1
                    right_max = right
        return res