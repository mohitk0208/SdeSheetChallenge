'''
################### Edit Distance ########################
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character


leetcode : https://leetcode.com/problems/edit-distance/

'''


# solution


# approach 1 : recursive (bottoms up)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)


        @cache
        def dp(i, j):   # this function returns the minimum operation required to convert word1[0..i] to word2[0..j] so we try all combinations and return minimum

            if i == 0:        # means word1 is empty so to convert we require j insert operations
                return j

            if j == 0:        # means word2 is empty so to convert we require i delete operations
                return i

            if word1[i-1] == word2[j-1]: # if the end letters are equal then no operation required
                return dp(i-1, j-1)


            x = 1 + dp(i, j-1)      # try insert operation
            y = 1 + dp(i-1, j-1)    # try replace operation
            z = 1 + dp(i-1, j)      # try delete operation

            return min(x, y, z)     # return the minimum of all combinations

        return dp(m, n)




# approach 2 : Top down
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        matrix = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            matrix[i][0] = i

        for j in range(n+1):
            matrix[0][j] = j


        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])

        return matrix[m][n]