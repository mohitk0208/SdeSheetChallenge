'''
############### Sliding Window Maximum ###############
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


 leetcode : https://leetcode.com/problems/sliding-window-maximum/

'''

# solution

# approach : brute force
# SC -> O(1) and TC -> O(n^2)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []

        for i in range(len(nums)-k+1):
            res.append(max(nums[i:i+k]))

        return res



# approach 2 : using deque
# SC -> O(k) and TC -> O(n)
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        window = deque()           # stores the element index of the window in descending order
                                   # it may hold < k elements

        i = 0
        while i < k:
            if len(window) == 0:
                window.append(i)   # if window is empty, add the element index
            else:
                while len(window) > 0 and nums[window[-1]] < nums[i]: # till the tail of window is less than the current element
                    window.pop()                                   # remove the tail of window

                window.append(i)     # add the current element index to the window
            i += 1

        res = [nums[window[0]]]

        while i < len(nums):
            if window[0] <= i-k:         # if the head of window is less than the current index minus k
                window.popleft()         # remove the head of window

            while len(window) > 0 and nums[window[-1]] < nums[i]:   # till the tail of window is less than the current element
                window.pop()                            # remove the tail of window

            window.append(i)                  # add the current element index to the window
            res.append(nums[window[0]])      # add the max element of the window to the result (i.e the front of window)

            i += 1

        return res
