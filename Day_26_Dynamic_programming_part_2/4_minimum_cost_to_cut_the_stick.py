'''
########################### Minimum Cost to Cut a Stick #####################
Given a wooden stick of length n units. The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:

Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.

You should perform the cuts in order, you can change the order of the cuts as you wish.

The cost of one cut is the length of the stick to be cut, the total cost is the sum of costs of all cuts. When you cut a stick, it will be split into two smaller sticks (i.e. the sum of their lengths is the length of the stick before the cut). Please refer to the first example for a better explanation.

Return the minimum total cost of the cuts.

example
Input: n = 7, cuts = [1,3,4,5]
Output: 16
Explanation: Using cuts order = [1, 3, 4, 5] as in the input leads to the following scenario:

The first cut is done to a rod of length 7 so the cost is 7. The second cut is done to a rod of length 6 (i.e. the second part of the first cut), the third is done to a rod of length 4 and the last cut is to a rod of length 3. The total cost is 7 + 6 + 4 + 3 = 20.
Rearranging the cuts to be [3, 5, 1, 4] for example will lead to a scenario with total cost = 16 (as shown in the example photo 7 + 4 + 3 + 2 = 16).


leetcode : https://leetcode.com/problems/minimum-cost-to-cut-a-stick/

'''


# solution
# approach 1 : recursive
# here dp(i, j) denotes the minimum cost to perform the cuts in the range `i` -> `j` to perform the cuts that are possible in the cuts array, if no cut in cuts array is possible then return 0 as no cut has been done so cost is 0
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @cache
        def dp(i, j):

            min_ = float("inf")
            for cut in cuts:                              # try every cut that is possible
                if i < cut < j:
                    cost = (j-i) + dp(i, cut) + dp(cut, j)
                    min_ = min(min_, cost)

            return 0 if min_ == float("inf") else min_    # if no cut was performed then return 0

        return dp(0, n)



# approach 2 : iterative (BUT TIME LIMIT GETS EXCEEDED)
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        matrix = [[0]*(n+1) for _ in range(n+1)]


        for i in range(n, -1, -1):
            for j in range(i+1, n+1):

                min_ = float("inf")
                for cut in cuts:
                    if i < cut < j :
                        cost = (j-i) + matrix[i][cut] + matrix[cut][j]

                        min_ = min(min_, cost)

                matrix[i][j] = 0 if min_ == float("inf") else min_

        return matrix[0][n]

