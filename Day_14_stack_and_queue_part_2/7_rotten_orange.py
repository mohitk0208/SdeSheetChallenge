'''
######################## Rotten Orange ###########################
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1


leetcode : https://leetcode.com/problems/rotting-oranges/

'''



# solution
# approach: BFS
from queue import Queue

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m, n = len(grid) , len(grid[0])
        INF = float("inf")

        vis = [[-1]*n for _ in range(m)]

        rotten = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                    vis[i][j] = 0           # rotten in the beginning i.e 0 mins
                elif grid[i][j] == 1:
                    vis[i][j] = INF         # initially all fresh oranges get rotten after INF mins


        for r in rotten:            # run BFS on rotten oranges
            q = Queue()
            q.put(r)

            while len(q.queue) != 0:
                x = q.get()
                newCount = vis[x[0]][x[1]] + 1

                for i, j in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                    nx = x[0] + i
                    ny = x[1] + j

                    if 0 <= nx < m and 0 <= ny < n:
                        if vis[nx][ny] != -1:
                            if newCount < vis[nx][ny]:
                                vis[nx][ny] = newCount
                                q.put((nx, ny))


        ans = 0
        for i in range(m):
            for j in range(n):
                if vis[i][j] == INF:
                    return -1
                ans = max(ans, vis[i][j])

        return ans
