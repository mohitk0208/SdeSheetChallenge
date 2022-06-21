'''
################################ 2 Sum Problem ######################

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

leetcode : https://leetcode.com/problems/two-sum/

'''


# leetcode solution
# approach 1 : brute force : try every pair
# SC -> O(1) and TC -> O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums) - 1):
            v = target - nums[i]
            for j in range(i+1, len(nums)):
                if v == nums[j]:
                    return [i, j]


# approach : using hashmap or dictionary
# explanation
#       if one number is x then the other is target-x, let it be v
#       now we need to find v's index, to improve searching we use hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        c = {}

        for i, v in enumerate(nums):
            x = target - v

            if x in c:
                return [i, c[x]]

            c[v] = i