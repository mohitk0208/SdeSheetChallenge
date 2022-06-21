'''
#################### Largest Subarray with 0 Sum ####################

Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.
Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

gfg : https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1#

'''

# solution
#approach 1 : brute force
# SC -> O(1) and TC -> O(n^3)
class Solution:
    def maxLen(self, n, arr):

        max_ = 0

        for i in range(n):              # O(n)
            for j in range(i+1, n+1):   # O(n)
                sum_ = sum(arr[i:j])  # O(n)

                if sum_ == 0:
                    max_ = max(max_, j-i)

        return max_



# approach 2 : using hashmap to store prefix sum and its index
# SC -> O(n) and TC -> O(n) + O(n) = O(n)

# concept
# for example the array is [15, -2, 2, -8, 1, 7, 10, 23]
# for index 0  sum is 15
# from index 0 to 2 sum is 15
# it means that the sum of subarray from index 1 to 2 is 0

# i.e If PREFIX_SUM + SUFFIX_SUM = PREFIX_SUM , then SUFFIX_SUM = 0


class Solution:
    def maxLen(self, n, arr):

        max_ = 0
        c = {}            # dictionary to store prefix sum and its index
        sum_ = 0
        for i,x in enumerate(arr):
            sum_ += x     # sum from start to current index

            if sum_ == 0:       # sum_ if 0 subarray is from start to current index
                max_ = max(max_, i+1)

            if sum_ in c:                         # if current sum is already present in dictionary then it means that,
                max_ = max(max_, i - c[sum_])     # the sum of values in between c[sum_] and i is 0 so max_ is updated
            else:
                c[sum_] = i               # storing prefix sum and its index

        return max_