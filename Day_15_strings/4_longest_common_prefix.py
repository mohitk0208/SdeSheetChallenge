'''
##################### Longest Common Prefix #####################
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"


leetcode : https://leetcode.com/problems/longest-common-prefix/

'''


# solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_ = min(list(map(len, strs)))

        for i in range(min_):
            c = strs[0][i]

            for s in strs:
                if s[i] != c:
                    return s[:i]

        return strs[0][:min_]