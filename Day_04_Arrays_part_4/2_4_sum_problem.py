'''
#################### 4 Sum Problem ######################

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

leetcode : https://leetcode.com/problems/4sum/

'''

# solution

# approach 1 : three pointers and binary search after sorting
# SC -> O(n) and TC -> O(n^3logn)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        nums.sort() # O(nlogn)

        res = set([])

        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    t = target - nums[i] - nums[j] - nums[k]

                    low = k + 1
                    high = n - 1

                    while low <= high:
                        mid = (low + high) // 2

                        if nums[mid] == t:
                            res.add((nums[i], nums[j], nums[k], nums[mid]))
                            break

                        if nums[mid] < t:
                            low = mid + 1
                        else:
                            high = mid - 1

        return res






# approach 2 : two pointers and two sum after sorting
# SC -> O(1) and TC -> O(n^3)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        res = set([])

        nums.sort()           # sorting O(nlogn)
        i = 0

        while i < n-3:              # O(n^3)
            j = i +1
            while j < n-2:          # O(n^2)
                t = target - nums[i] - nums[j]

                left = j+1
                right = n-1

                while left < right:     #O(n)
                    sum_ = nums[left] + nums[right]
                    if sum_ == t:
                        res.add((nums[i], nums[j], nums[left], nums[right]))  # add unique solutions to the set

                        curr = nums[left]
                        while left < n and nums[left] == curr:
                            left += 1

                        curr = nums[right]
                        while right > j and nums[right] == curr:
                            right -= 1

                    elif sum_ > t:                    # if the sum_ is greater than t, then we need to move the right pointer to the left so as to DECREASE the value of sum_
                        curr = nums[right]
                        while right > j and nums[right] == curr:
                            right -= 1
                    else:                             # if the sum_ is less than t, then we need to move the left pointer to the right so as to INCREASE the value of sum_
                        curr = nums[left]
                        while left < n and nums[left] == curr:
                            left += 1

                curr = nums[j]
                while j < n and nums[j] == curr:
                    j += 1

            curr = nums[i]
            while i < n and nums[i] == curr:
                i += 1

        return res