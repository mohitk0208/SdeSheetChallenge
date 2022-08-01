'''
######################## Longest Common Subsequence ###################
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.


leetcode : https://leetcode.com/problems/longest-common-subsequence/

'''

# solution

# approach 1 : recursive with memoization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        matrix = [[-1]*(n+1) for _ in range(m+1)] # table for memoization


        def lcs(i, j):
            if i == 0 or j == 0:    # base condition
                return 0

            if matrix[i][j] != -1:
                return matrix[i][j]     # using memoized value

            ans = 0
            if text1[i-1] == text2[j-1]:  # condition for recursive call
                ans = 1 + lcs(i-1, j-1)
            else:
                ans = max(lcs(i-1, j), lcs(i, j-1))

            matrix[i][j] = ans      # memoization

            return ans        # return the ans

        return lcs(m, n)





# approach 2 :  Top Down tabulation
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        matrix = [[-1]*(n+1) for _ in range(m+1)] # matrix formation

        # ------- Initialization ----------
        for i in range(m+1):
            matrix[i][0] = 0

        for j in range(n+1):
            matrix[0][j] = 0

        # ----------------------------------


        # solving subproblems using the values of previously solved problem
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    matrix[i][j] = 1 + matrix[i-1][j-1]
                else:
                    matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j])

        # the right bottom contain the required answer
        return matrix[m][n]