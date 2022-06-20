'''
####################### Number of Islands #################
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

leetcode : https://leetcode.com/problems/number-of-islands/

'''


# solution
# approach : DFS
# -> run dfs for every unvisited node that has a value of 1 and increment the count
# -> in dfs run dfs for all horizontally and vertically adjacent nodes that have a value of 1
# ->
# SC -> O(m*n) and TC -> O(m*n)
class Solution:

    def dfs(self, i, j, vis, grid):
        vis[i][j] = True
        n, m = len(grid), len(grid[0])

        if i > 0:
            if not vis[i-1][j] and grid[i-1][j] == "1":
                self.dfs(i-1, j, vis, grid)

        if i < n-1:
            if not vis[i+1][j] and grid[i+1][j] == "1":
                self.dfs(i+1, j, vis, grid)

        if j > 0:
            if not vis[i][j-1] and grid[i][j-1] == "1":
                self.dfs(i, j-1, vis, grid)

        if j < m-1:
            if not vis[i][j+1] and grid[i][j+1] == "1":
                self.dfs(i, j+1, vis, grid)




    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n, m = len(grid), len(grid[0])

        vis = [[False]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == "1":
                    self.dfs(i, j, vis, grid)
                    count += 1

        return count