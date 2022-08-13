'''
################## Print all permutations of a array/list ##############
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]



leetcode : https://leetcode.com/problems/permutations/

'''


# solution
# approach 1 :  using itertools in python
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        for x in permutations(nums):
            res.append(x)

        return res



# approach 2 : using recursion and set
# SC -> O(N!*N) and TC -> O(N!*N)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def construct(s, curr):
            if len(s) == 0:
                ans.append(curr[:])
                return

            for x in list(s):
                curr.append(x)
                s.remove(x)
                construct(s, curr)
                s.add(x)
                curr.pop()

        construct(set(nums), [])

        return ans