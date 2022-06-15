'''
################## Search in 2D Matrix ##################

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

-> Integers in each row are sorted from left to right.
-> The first integer of each row is greater than the last integer of the previous row.

leetcode : https://leetcode.com/problems/search-a-2d-matrix/
codestudio : https://www.codingninjas.com/codestudio/problems/980531?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=1

'''

# leetcode solution
# use binary search to find the target
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l = m * n

        low = 0
        high = l - 1

        while low <= high:
            mid = (low + high) // 2

            i = mid // n
            j = mid % n

            if matrix[i][j] == target:
                return True

            if matrix[i][j] < target:
                low = mid + 1
            else:
                high = mid - 1


        return False