'''
#################### Flood fill ##################
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.


leetcode : https://leetcode.com/problems/flood-fill/

'''


# solution
# approach : dfs
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        self.m, self.n = len(image), len(image[0])

        self.initial = image[sr][sc]

        self.vis = [[False]*self.n for _ in range(self.m)]


        def dfs(i, j):
            if not (0 <= i < self.m) or not (0 <= j < self.n ):
                return

            if image[i][j] == self.initial and not self.vis[i][j]:
                image[i][j] = color
                self.vis[i][j] = True
            else:
                return

            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                dfs(i + x, j + y)


        dfs(sr, sc)

        return image