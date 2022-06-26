'''
############### 3 Sum problem ###############
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

leetcode : https://leetcode.com/problems/3sum/

'''


# solution
# SC -> O(n) and TC -> O(nlogn) + O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set([])
        nums.sort()


        i  = 0

        while i < n-2:
            t = 0 - nums[i]

            left = i + 1
            right = n -1

            while left < right:
                sum_ = nums[left] + nums[right]

                if sum_ == t:
                    res.add((nums[i], nums[left], nums[right]))

                    curr = nums[left]
                    while left < n and nums[left] == curr:
                        left += 1

                    curr = nums[right]
                    while right > i and nums[right] == curr:
                        right -= 1

                elif sum_ > t:
                    curr = nums[right]
                    while right > i and nums[right] == curr:
                        right -= 1
                else:
                    curr = nums[left]
                    while left < n and nums[left] == curr:
                        left += 1

            curr = nums[i]
            while i < n-2 and nums[i] == curr:
                i += 1

        return list(res)

