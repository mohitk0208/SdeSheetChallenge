'''
######################## Count Unique Paths #########################
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

leetcode : https://leetcode.com/problems/unique-paths/

'''

# solution
# approach 1 : using maths (permutation and combination)
# SC -> O(1) and TC -> O(n)
# total_paths = (m + n)! / (m! * n!), where m = number of down steps and n = number of right steps
from math import factorial as fac
class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        nr = n-1
        nd = m-1

        return fac(nr+nd) // (fac(nr) * fac(nd))


# approach 2 : using dynamic programming
