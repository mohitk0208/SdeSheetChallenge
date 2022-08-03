'''
################################## Partition Equal Subset sum ###############
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.


Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.



leetcode : https://leetcode.com/problems/partition-equal-subset-sum/

'''



# solution
# approach 1 : recursive (Bottoms up)
# here dp(i, ss) return whether we can get sum as `ss` if we pick elements from `ith` index to the end
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        s = sum(nums)

        @cache
        def dp(i, ss):
            if i == n:
                if ss == 0:
                    return True

                return False

            if ss == 0:
                return True

            if nums[i] <= ss:
                return dp(i+1, ss) or dp(i+1, ss-nums[i])

            return dp(i+1, ss)

        if s % 2 == 0:
            return dp(0, s // 2)

        return False





# approach 2 : recursive
# here dp(i, ss) denotes if it is possible to achieve sum as `ss` if we use starting `i` elements of the nums array
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        s = sum(nums)

        def dp(i, ss):
            if ss == 0:
                return True

            if i == 0:
                return False

            if nums[i-1] <= ss:
                return dp(i-1, ss-nums[i-1]) or dp(i-1, ss)

            return dp(i-1, ss)

        if s&1 == 0:                                    # Efficient method to check for even and odd
            return dp(len(nums), s //2 )

        return False






# approach 3 : iterative for approach 2
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        s = sum(nums)
        if s % 2 != 0:
            return False

        ss = s // 2


        matrix = [[False]*(ss+1) for _ in range(len(nums)+1)]

        for i  in range(len(nums)+1):
            matrix[i][0] = True


        for i in range(1, len(nums)+1):
            for j in range(1, ss +1):
                if j >= nums[i-1]:
                    matrix[i][j] = matrix[i-1][j-nums[i-1]] or matrix[i-1][j]
                else:
                    matrix[i][j] = matrix[i-1][j]


        return matrix[len(nums)][ss]
