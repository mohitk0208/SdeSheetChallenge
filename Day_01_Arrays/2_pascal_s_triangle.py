'''

################################ Pascal's Triangle #################################

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it

example:
1
1 1
1 2 1
1 3 3 1

Here for the third row, you will see that the second element is the summation of the above two-row elements i.e. 2=1+1, and similarly for row three 3 = 1+2 and 3 = 1+2.

leetcode : https://leetcode.com/problems/pascals-triangle/
codestudio : https://www.codingninjas.com/codestudio/problems/1089580?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

'''

# leetcode solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]

        res = [[1], [1, 1]]

        for i in range(2, numRows):
            x = [1]

            for j in range(1, i):
                x.append(res[i-1][j-1] + res[i-1][j])

            x.append(1)

            res.append(x)

        return res