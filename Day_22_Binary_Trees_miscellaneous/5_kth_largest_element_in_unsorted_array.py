'''
####################### Kth largest element in unsorted array ###############
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.


leetcode : https://leetcode.com/problems/kth-largest-element-in-an-array/

'''


# solution
# approach 1 : using heap
from heapq import heappush, heappop, heapify

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        vals = []
        heapify(vals)

        for n in nums:
            heappush(vals, -n)

        for _ in range(k-1):
            heappop(vals)

        return -1*heappop(vals)