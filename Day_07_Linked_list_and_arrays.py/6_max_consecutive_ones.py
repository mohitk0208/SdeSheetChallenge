'''
################# Max consecutive ones #################
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

leetcode : https://leetcode.com/problems/max-consecutive-ones/

'''


# solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ = 0
        count = 0

        for x in nums:
            if x == 0:
                count = 0
            else:
                count += 1
                max_ = max(max_, count)

        return max_

