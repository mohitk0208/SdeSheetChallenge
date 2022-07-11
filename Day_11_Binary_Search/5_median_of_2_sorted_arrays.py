'''
########################## Median of 2 Sorted Arrays ##########################
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


leetcode : https://leetcode.com/problems/median-of-two-sorted-arrays/

'''



# solution
# approach : merge two sorted arrays (Naive approach)
# SC -> O(m+n) and TC -> O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while i < len(nums1):
            nums.append(nums1[i])
            i += 1

        while j < len(nums2):
            nums.append(nums2[j])
            j += 1


        if (len(nums)) % 2 != 0:
            return nums[len(nums) // 2]


        x = len(nums) // 2
        return (nums[x-1] + nums[x]) / 2




# approach 2 : merge two sorted arrays (optimized naive approach )
# SC -> O(1) and TC -> O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)
        i = 0
        j = 0
        t = m+n

        pick = set([t//2, t//2 -1]) if t % 2 == 0 else set([t//2])
        count = -1
        ele = []

        while i < m and j < n and len(pick) != 0:
            count += 1
            if nums1[i] <= nums2[j]:
                if count in pick:
                    ele.append(nums1[i])
                    pick.remove(count)
                i += 1
            else:
                if count in pick:
                    ele.append(nums2[j])
                    pick.remove(count)

                j +=1

        while i < m  and len(pick) != 0:
            count += 1
            if count in pick:
                ele.append(nums1[i])
                pick.remove(count)
            i += 1

        while j < n and len(pick) != 0:
            count += 1
            if count in pick:
                ele.append(nums2[j])
                pick.remove(count)
            j += 1

        if len(ele) == 1: return ele[0]

        return sum(ele)/2