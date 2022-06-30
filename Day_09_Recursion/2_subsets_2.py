'''
################# Subsets II #################
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order
Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]


leetcode : https://leetcode.com/problems/subsets-ii/

'''


# solution
# SC -> O(2^n) and TC -> O(2^n)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = set([])

        def subsets(arr, curr_arr, curr):
            if curr == len(arr):
                ans.add(tuple(curr_arr))
                return

            subsets(arr, curr_arr, curr+1)
            subsets(arr, curr_arr+[arr[curr]], curr+1)

        subsets(nums, [], 0)

        return ans