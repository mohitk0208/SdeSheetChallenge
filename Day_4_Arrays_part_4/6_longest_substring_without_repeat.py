'''
###################### Longest Substring Without Repeat ######################
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

leetcode : https://leetcode.com/problems/longest-substring-without-repeating-characters/

'''


# solution
# SC -> O(n) and TC -> O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = {}

        start = -1
        end = 0
        max_ = 0

        while end < len(s):
            if s[end] in c:
                max_ = max(max_, end-start-1)
                if c[s[end]] > start:
                    start = c[s[end]]
                c[s[end]] = end
            else:
                c[s[end]] = end

            end += 1

        max_ = max(max_, end - start-1)

        return max_