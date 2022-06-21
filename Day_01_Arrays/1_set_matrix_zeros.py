'''

######################### Set Matrix Zeros #########################

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

leetcode : https://leetcode.com/problems/set-matrix-zeroes/
codestudio: https://www.codingninjas.com/codestudio/problems/set-matrix-zeros_3846774?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

'''

# Leetcode solution
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        rows = set([])              # store the rows that need to be set to zero
        columns = set([])           # store the columns that need to be set to zero


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)       # add the row to the set
                    columns.add(j)    # add the column to the set

        for i in range(m):
            if i in rows:
                for j in range(n):    # set the row to zero
                    matrix[i][j] = 0
            else:
                for j in range(n):
                    if j in columns:    # set the column to zero
                        matrix[i][j] = 0