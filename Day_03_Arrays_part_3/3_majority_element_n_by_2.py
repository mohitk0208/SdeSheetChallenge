'''

################ Majority element > n/2 times ################
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


leetcode : https://leetcode.com/problems/majority-element/

'''

# solution

# approach 1 : using dictionary
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)

        max_ = (-1, -1)
        for x in c.keys():
            if c[x] > max_[1]:
                max_ = (x, c[x])

        return max_[0]





# approach 2 :  Boyer-Moore Voting Algorithm
# here the approach is that we store the current majority element and its count
# if current element is same as majority element, we increment the count
# if current element is different from majority element, we decrement the count
# if count becomes 0, we update the majority element and its count
# Explanation :
#   since the majority element is present more than n / 2 times, it means all other elements are present < n / 2 times
#   count for the majority element will stay positive while for other elements it will become 0 or
#   will be less than majority element and hence not be a majority element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count, major = 0, nums[0]

        for x in nums:
            if count == 0:
                major = x

            if major == x:
                count += 1
            else:
                count -= 1

        return major