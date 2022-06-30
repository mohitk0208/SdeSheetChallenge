'''
################### Subsets Sum ###################
Given a list arr of N integers, print sums of all subsets in it.

Example 1:

Input:
N = 2
arr[] = {2, 3}
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then
Sum = 2+3 = 5.


gfg : https://practice.geeksforgeeks.org/problems/subset-sums2234/1#

'''


# solution
# approach 1 : without recursion (using itertools)
# SC -> O(2^n) and TC -> O(n2^n)
from itertools import combinations

class Solution:
  def subsetSums(self, arr, N):
    ans = [0]

    for i in range(1, N+1):
      comb = combinations(arr, i)

      for x in comb:
          ans.append(sum(x))

    return ans






# approach 2 : with recursion
# SC -> O(2^n) and TC -> O(2^n)
class Solution:
    def subsetSums(self, arr, N):
        ans = []

        def subsets(arr, curr, sum_):
            if curr == len(arr):
                ans.append(sum_)
                return

            subsets(arr, curr+1, sum_)
            subsets(arr, curr+1, sum_+arr[curr])


        subsets(arr, 0, 0)

        return ans
