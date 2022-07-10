'''
################### Single element in sorted array ###################
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

leetcode : https://leetcode.com/problems/single-element-in-a-sorted-array/

'''


# solution
# approach 1 : XOR, repeating elements will get canceled out and the non-repeating is left in the end
# SC -> O(1) and TC -> O(n)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xor_arr = 0

        for v in nums:
            xor_arr ^= v

        return xor_arr




# approach 2 : Binary Search
# SC -> O(1) and TC -> O(logn)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:


        low = 0
        high = len(nums) - 1
        mid = 0
        while low <= high:
            mid = (low+high) // 2

            if mid > 0 and nums[mid-1] == nums[mid]:
                if mid % 2 == 0:
                    high = mid - 1
                else:
                    low = mid + 1
            elif mid < len(nums) - 1 and nums[mid+1] == nums[mid]:
                if mid % 2 == 0:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                return nums[mid]


        return nums[mid]