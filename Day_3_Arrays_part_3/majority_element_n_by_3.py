'''
################################# Majority element > n/ 3 times #################################
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

leetcode : https://leetcode.com/problems/majority-element-ii/

'''


# solution

#approach 1 : using dictionary
# SC -> O(n) and TC -> O(n)
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        c = Counter(nums)

        min_ = len(nums) / 3

        res = []

        for k,v in c.items():
            if v > min_:
                res.append(k)

        return res



# approach 2 : Extended Boyer Moore’s Voting Algorithm
# SC -> O(1) and TC -> O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        num1 = nums[0]
        num2 = nums[0]
        n = len(nums)
        c1, c2 = 0, 0

        for x in nums:
            if x == num1:
                c1 += 1
            elif x == num2:
                c2 += 1
            elif c1 == 0 :
                num1 = x
                c1 = 1
            elif c2 == 0:
                num2 = x
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        c1 = c2 = 0

        for x in nums:
            if x == num1:
                c1 += 1
            elif x == num2:
                c2 += 1

        res = []
        if c1 > n / 3:
            res.append(num1)

        if c2 > n / 3:
            res.append(num2)

        return res