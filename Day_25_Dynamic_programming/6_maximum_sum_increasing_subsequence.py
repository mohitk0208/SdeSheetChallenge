'''
#################### Maximum Sum increasing subsequence ################
Given an array of n positive integers. Find the sum of the maximum sum subsequence of the given array such that the integers in the subsequence are sorted in strictly increasing order i.e. a strictly increasing subsequence.

Input: N = 5, arr[] = {1, 101, 2, 3, 100}
Output: 106
Explanation:The maximum sum of a
increasing sequence is obtained from
{1, 2, 3, 100}

gfg : https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1

'''


# solution
# approach 1 : recursion with memoization
class Solution:
  def maxSumIS(self, Arr, n):
    max_sum = [-1 for _ in range(n)]

    def dp(i):
        if i == n:
            return 0

            if max_sum[i] != -1:
                return max_sum[i]

            max_ = Arr[i]
            for j in range(i+1, n):
                if Arr[j] > Arr[i]:
                    x = Arr[i] + dp(j)

                    max_ = max(max_, x)

            max_sum[i] = max_

            return max_

        ans = 0
        for index in range(n):
            ans = max(ans, dp(index))

        return ans