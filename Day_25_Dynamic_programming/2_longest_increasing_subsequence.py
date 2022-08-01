'''
##################### Longest Increasing Subsequence ######################
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Input: nums = [0,1,0,3,2,3]
Output: 4


leetcode : https://leetcode.com/problems/longest-increasing-subsequence/

'''



# solution

# approach : recursive approach with memoization
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        max_len = [0 for _ in range(n)]

        def max_val(index):
            if index == n-1:
                return 1

            if max_len[index] != 0:
                return max_len[index]


            max_ = 1
            for i in range(index+1, n):
                if nums[i] > nums[index]:
                    val = 1 + max_val(i)

                    max_ = max(max_, val)

            max_len[index] = max_

            return max_

        ans = 0
        for i in range(n):
            ans = max(ans, max_val(i))

        return ans



# approach 2 : Top Down (tabulation)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        max_len = [1 for _ in range(n)]

        ans = 1
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    val = 1 + max_len[j]

                    max_len[i] = max(max_len[i], val)

            ans = max(ans, max_len[i])

        return ans