'''
####################### Minimum Path Sum ##########################
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.


leetcode : https://leetcode.com/problems/minimum-path-sum/


'''


# solution
# approach 1 : recursive (memoization)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        @cache
        def dp(i, j):

            if i == m-1 and j == n-1:
                return grid[i][j]

            min_ = float("inf")
            if i < m and j < n:
                min_ = min(min_, grid[i][j] + min(dp(i+1, j), dp(i, j+1)))

            return min_


        return dp(0, 0)



# approach 2 : Top Down
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        matrix = [[float("inf")]*(n+1) for _ in range(m+1) ]

        matrix[m-1][n-1] = grid[-1][-1]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue

                matrix[i][j] = grid[i][j] + min(matrix[i+1][j], matrix[i][j+1])


        # backtracking

        # --------------------------------------------------------------
        # if the code also asked to print the moves to reach the destination in minimum steps
        # --------------------------------------------------------------
        # stack = []

        # i = m-1
        # j = n-1
        # while i > 0 and j > 0:
        #     if matrix[i-1][j] < matrix[i][j-1]:
        #         stack.append("down")
        #         i -= 1
        #     else:
        #         stack.append("right")
        #         j -= 1

        # while i > 0:
        #     stack.append("down")
        #     i -= 1

        # while j > 0 :
        #     stack.append("right")
        #     j -= 1

        # stack.reverse()
        # print(stack)

        # --------------------------------------------------------------------



        return matrix[0][0]