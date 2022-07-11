'''
#################### Kth largest element in an array ####################
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

leetcode : https://leetcode.com/problems/kth-largest-element-in-an-array/

'''


# solution
# using heapq module
from heapq import heappush, heappop, heapify

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        vals = []
        heapify(vals)

        # to implement max heap push -ve of each value in the heap
        for n in nums:
            heappush(vals, -n)

        for _ in range(k-1):
            heappop(vals)     # pop the top k-1 element from the heap

        return -1*heappop(vals)    # return the kth element