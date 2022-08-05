'''
##################### Palindrome Partitioning ###################
Given a string str, a partitioning of the string is a palindrome partitioning if every sub-string of the partition is a palindrome. Determine the fewest cuts needed for palindrome partitioning of the given string.

Input: str = "ababbbabbababa"
Output: 3
Explaination: After 3 partitioning substrings
are "a", "babbbab", "b", "ababa".


gfg : https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1

'''


# solution
# approach 1 : recursive
class Solution:

    def palindromicPartition(self, string):

        n = len(string)
        matrix = [[-1]*(n+1) for _ in range(n+1)]

        def dp(i,j):
            if i == j:
                return 0

            if matrix[i][j] != -1:
                return matrix[i][j]

            v = string[i:j]
            if v == v[::-1]:
                return 0

            min_ = float("inf")
            for k in range(i+1, j+1):
                v = string[i:k]
                if v == v[::-1]:
                    min_ = min(min_, 1 + dp(k, j))

            matrix[i][j] = min_

            return min_


        return dp(0, len(string))
