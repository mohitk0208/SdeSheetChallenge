'''
####################### Reverse the words in the string #######################
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


leetcode : https://leetcode.com/problems/reverse-words-in-a-string/

'''



# solution
# approach : using re module
import re

class Solution:
    def reverseWords(self, s: str) -> str:
        words = re.split("\s+", s.strip())

        words.reverse()

        return " ".join(words)