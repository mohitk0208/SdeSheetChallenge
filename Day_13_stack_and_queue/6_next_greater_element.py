'''
########################## Next Greater element ####################
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]


leetcode : https://leetcode.com/problems/next-greater-element-i/V

'''

# solution
# SC -> O(2n) and Tc -> O(n) + O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ngr = []                          # store next greater element of each element in nums2

        stack = []
        c = {}                            # store index of each element in nums2

        for i in range(len(nums2)-1, -1, -1):
            if len(stack) == 0:
                ngr.append(-1)
            elif stack[-1] > nums2[i]:
                ngr.append(stack[-1])
            else:
                while len(stack) > 0 and stack[-1] <= nums2[i]:
                    stack.pop()

                if len(stack) == 0:
                    ngr.append(-1)
                else:
                    ngr.append(stack[-1])

            stack.append(nums2[i])
            c[nums2[i]] = i

        ngr.reverse()
        ans = []

        for x in nums1:
            ans.append(ngr[c[x]])

        return ans