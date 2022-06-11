'''
######################## Rotate Matrix ##########################

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

leetcode : https://leetcode.com/problems/rotate-image/

approach :
    1. transpose the matrix
    2. reverse the rows

explanation:
  1 2 3
  4 5 6
  7 8 9

  |
  |   Tanspose (convet rows to column and columns to rows)
 \|/

  1 4 7
  2 5 8
  3 6 9

  |
  |   Reverse the rows
 \|/

  7 4 1
  8 5 2
  9 6 3
'''

# leetcode solution (transpose -> reverse rows)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def swap(f, s):
            matrix[f[0]][f[1]], matrix[s[0]][s[1]] = matrix[s[0]][s[1]], matrix[f[0]][f[1]]

        for i in range(n):               # transpose the matrix
            for j in range(i):
                swap((i, j ), (j, i))

        for i in range(n):              # reverse each row
            matrix[i].reverse()


# leetcode solution (use an extra duplicate matrix) O(n^2)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        res = []

        for j in range(n):
            val = []
            for i in range(n-1, -1, -1):
                val.append(matrix[i][j])

            res.append(val)

        for i in range(n):
            for j in range(n):
                matrix[i][j] = res[i][j]

# rotate the corners
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 -j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp


'''
codestudio question
'''
# codestudio solution