'''

########################## Merge Two Sorted Arrays ##########################
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

leetcode : https://leetcode.com/problems/merge-sorted-array/

approach :
    sort from back of the array to front

'''

#leetcode solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # starting from the back of the array
        # and moving towards start
        i = m-1
        j = n-1
        k = m+n -1

        while i >= 0 and j >= 0:          # while both arrays are not empty
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1


        if j >= 0:
            nums1[:k+1] = nums2[:j+1]
