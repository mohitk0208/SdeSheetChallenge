'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

leetcode : https://leetcode.com/problems/trapping-rain-water/

'''

# solution
# SC -> O(3n) and TC -> O(4n)
class Solution:
    def trap(self, height: List[int]) -> int:
        mxl = []
        for h in height:
            if len(mxl) == 0:
                mxl.append(h)
                continue

            mxl.append(max(mxl[-1], h))

        mxr = []
        for h in height[::-1]:
            if len(mxr) == 0:
                mxr.append(h)
                continue

            mxr.append(max(mxr[-1], h))

        mxr.reverse()


        w = [0] * len(height)

        for i in range(len(height)):
            w[i] = min(mxr[i], mxl[i]) - height[i]

        return sum(w)





# approach 2 : using two pointers (most optimized approach)
# SC -> O(1) and TC -> O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        # using two pointers

        left = 0
        right = len(height) - 1

        ans = 0
        left_max = 0
        right_max = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1

            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1

        return ans