'''
########################### Kadaan's Algorithm ###########################

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

leetcode : https://leetcode.com/problems/maximum-subarray/
codestudio : https://www.codingninjas.com/codestudio/problems/630526?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
'''

# leetcode solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]                # set max to first element
        curr_sum = nums[0]            # set current sum to first element

        for i in range(1, len(nums)):

            curr_sum = max(curr_sum + nums[i], nums[i])
            max_ = max(max_, curr_sum)

        return max_



# codestudio solution
from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :

	# Your code here
    # return the answer
    max_ = arr[0]
    curr_sum = arr[0]

    for i in range(1, len(arr)):
        curr_sum = max(curr_sum+arr[i], arr[i])
        max_ = max(max_, curr_sum)

    return 0 if max_ < 0 else max_
