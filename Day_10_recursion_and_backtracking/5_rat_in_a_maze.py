'''
######################## Rat in a maze ####################
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.


Your Task:
You don't need to read input or print anything. Complete the function printPath() which takes N and 2D array m[ ][ ] as input parameters and returns the list of paths in lexicographically increasing order.
Note: In case of no path, return an empty list. The driver will output "-1" automatically.

Expected Time Complexity: O((3^(N^2))).
Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths

gfg : https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

'''

# solution
# approach 1 : recursive
class Solution:
    def findPath(self, m, n):
        if m[0][0] == 0:
            return []

        vis = [[False]*n for _ in range(n) ]

        ans = []
        def dp(i, j, curr):
            if not (0<=i<n and 0<= j <n):
                return

            if m[i][j] == 0 or vis[i][j] == True:
                return

            if i == n-1 and j == n-1:
                ans.append("".join(curr))
                return

            vis[i][j] = True
            for x, y, move in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
                curr.append(move)
                dp(i+x, j+y, curr)
                curr.pop()

            vis[i][j] = False

        dp(0, 0, [])
        return ans