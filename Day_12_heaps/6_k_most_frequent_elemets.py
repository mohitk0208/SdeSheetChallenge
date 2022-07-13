'''
#################### K most frequent elements ####################
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


leetcode : https://leetcode.com/problems/top-k-frequent-elements/

'''


# solution
from heapq import heapify, heappop, heappush
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        l = []

        heapify(l)

        for x,f in c.items():
            heappush(l, (-f, x))

        res = []
        for _ in range(k):
            res.append(heappop(l)[1])

        return res



# approach : using heap but optimized
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)


        return heapq.nlargest(k, c.keys(), key= c.get)