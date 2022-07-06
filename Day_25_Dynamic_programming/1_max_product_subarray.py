'''
#################### Max product Subarray ####################
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.


leetcode : https://leetcode.com/problems/maximum-product-subarray/

'''




# solution
# approach : Brute Force
# SC -> O(1) and TC -> O(n^2)
class Solution:
    def maxProduct(self, nums):
        for i in range(len(nums)):
            curr = 1
            for j in range(i, len(nums)):
                curr *= nums[j]

                max_ = max(max_, curr)

        return max_



# approach : modified Kadane's algorithm
# SC -> O(1) and TC -> O(n)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curr_max = 1                      # current max product
        curr_min = 1                      # current min product
        res = float("-inf")

        for num in nums:
            temp_max = curr_max * num
            temp_min = curr_min * num
            curr_max = max(temp_max, temp_min, num)   # max can be the `num`, `product of curr max subarray and num`, `product of curr min subarray and num`
            curr_min = min(temp_max, temp_min, num) # min can be the `num`, `product of curr max subarray and num`, `product of curr min subarray and num`

            res = max(res, curr_max) # update res

        return res