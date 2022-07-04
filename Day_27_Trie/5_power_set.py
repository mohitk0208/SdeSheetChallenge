'''
###################### Power Set ######################
Given a string S, Find all the possible subsequences of the String in lexicographically-sorted order.
You don't need to read input or print anything. Your task is to complete the function AllPossibleStrings() which takes S as the input parameter and returns a list of all possible substrings(non-empty) that can be formed from S in lexicographically-sorted order.

Expected Time Complexity: O(2n) where n is the length of the String
Expected Space Complexity: O(n * 2n)

Example 1:

Input : str = "abc"
Output: a ab abc ac b bc c
Explanation : There are 7 subsequences that
can be formed from abc.

gfg : https://practice.geeksforgeeks.org/problems/power-set4302/1#

'''


# solution
# approach 1: Brute Force
# SC -> O(2^n) and TC -> O(2^n) + O(nlog(n))
class Solution:
  def AllPossibleStrings(self, s):
    ans = []
    for i in range(len(s)):
      res = []                        # res is the list of all possible subsequences starting from i

      for j in range(i, len(s)):
        if len(res) == 0:
          res.append(s[i])            # if res is empty, add the first character
        else:
          y = []                     # create a new word by adding current character to each word in res and append it to y
          for word in res:
            y.append(word + s[j])

          res.extend(y)             # add the new words to res

      ans.extend(res)               # add the words in res to ans

    ans.sort()                      # sort the ans
    return ans