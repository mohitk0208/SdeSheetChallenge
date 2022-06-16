'''
############################### next permutation ###############################

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

leetcode : https://leetcode.com/problems/next-permutation/
codestudio : https://www.codingninjas.com/codestudio/problems/893046?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

'''

# Leetcode Solution

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        x = None
        y = None

        for i in range(len(nums) - 1, 0, -1):     # iterate from reverse and find the first element index
            if nums[i] > nums[i-1]:               # where the trend of ascending order is broken
                x = i-1
                y = i
                break


        if x == None:                 # means the list is in descending order
            nums.reverse()            # so convert the list to ascending order
            return

        swpIdx = len(nums) - 1
        for i in range(y, len(nums)):     # find the index for the smallest element that is greater than nums[x]
            if nums[i] > nums[x]:
                swpIdx = i

        nums[x], nums[swpIdx] = nums[swpIdx], nums[x] # swap the elements

        i = y
        j = len(nums) - 1

        while i < j:                      # reverse the list from y to the end
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


# example:
'''

- 1 5 8 4 7 6 5 3 1             // find the first element index where the trend of ascending order is broken
- 1 5 8 5 7 6 4 3 1             // swap the elements
- 1 5 8 5 1 3 4 6 7             // reverse the list from y to the end

'''

# codestudio Solution
from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(permutation, n):
    x = None
    y = None

    for i in range(len(permutation) - 1, 0, -1):
        if permutation[i] > permutation[i-1]:
            x = i-1
            y = i
            break


    if x == None:
        permutation.reverse()
        return permutation

    swpIdx = len(permutation) - 1
    for i in range(y, len(permutation)):
        if permutation[i] > permutation[x]:
            swpIdx = i

    permutation[x], permutation[swpIdx] = permutation[swpIdx], permutation[x]

    i = y
    j = len(permutation) - 1

    while i < j:
        permutation[i], permutation[j] = permutation[j], permutation[i]
        i += 1
        j -= 1

    return permutation