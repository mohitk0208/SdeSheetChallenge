'''
########################### Palindrome Partitioning ######################
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]


leetcode : https://leetcode.com/problems/palindrome-partitioning/

'''


# solution
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = set([])

        def isPalindrome(y):
            if len(y) <= 1:
                return True

            for i in range(len(y) // 2):
                if y[i] != y[len(y)-1-i]:
                    return False

            return True


        def combinations(curr_arr, s, start):
            if start >= len(s):
                ans.add(tuple(curr_arr))
                return


            for end in range(start, len(s)):
                ss = s[start: end+1]

                if isPalindrome(ss):
                    curr_arr.append(ss)
                    combinations(curr_arr, s, end+1)
                    curr_arr.pop()


        combinations([], s, 0)