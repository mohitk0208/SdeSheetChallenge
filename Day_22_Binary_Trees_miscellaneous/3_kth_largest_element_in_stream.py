'''
#################### Kth largest element in stream ################
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.


leetcode : https://leetcode.com/problems/kth-largest-element-in-a-stream/

'''


# solution
# approach 1 : using insort from bisect library
from bisect import insort

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()

    def add(self, val: int) -> int:
        # takes more time
        insort(self.nums, val)    # it always stores the list in sorted array

        return self.nums[-self.k]


# approach 2 : using min heap and maintaining k elements at a time
from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = []
        self.k = k
        heapify(self.q)

        for n in nums:
            heappush(self.q, n)

        # store only k elements
        while len(self.q) > self.k:
            heappop(self.q)

    def add(self, val: int) -> int:
        heappush(self.q, val)

        while len(self.q) > self.k:
            heappop(self.q)

        # since `q` has only k elements so kth largest is the first element or the minium element of self.q
        return self.q[0]