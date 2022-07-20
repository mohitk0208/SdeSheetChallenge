'''
####################### Longest Palindrome in a String #######################
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"


leetcode : https://leetcode.com/problems/longest-palindromic-substring/

'''



# solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_ = 0
        ans = ""
        n = len(s)

        for i in range(len(s)):
            count = 1
            l = i - 1
            r = i + 1

            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                count += 2
                l -= 1
                r += 1

            if count > max_:
                ans = s[l+1:r]
                max_ = count


        for i in range(n-1):
            if s[i] != s[i+1]:
                continue

            count = 2
            l = i - 1
            r = i + 2

            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                count += 2
                l -= 1
                r += 1

            if count > max_ :
                ans = s[l+1:r]
                max_ = count

        return ans
