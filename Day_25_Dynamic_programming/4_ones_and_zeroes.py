'''
#################### Ones and Zeroes ########################
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.


leetcode : https://leetcode.com/problems/ones-and-zeroes/

'''


# solution

# approach 1 : Recursive with memoization
from collections import Counter

class Solution:
    def findMaxForm(self, strs: List[str], x: int, y: int) -> int:

        l = len(strs)
        d = {}

        def sol(i, m, n ):

            if i == l:
                return 0

            s = f'{i}_{m}_{n}'
            if s in d:
                return d[s]

            c = Counter(strs[i])

            zeroes = c.get('0', 0 )
            ones = c.get('1', 0)

            ans = 0
            if zeroes <= m and ones <= n :
                ans = max(1 + sol(i+1, m-zeroes, n-ones), sol(i+1, m, n))
            else:
                ans = sol(i+1, m, n)

            d[s] = ans

            return ans



        return sol(0, x, y)


# approach 2 : The above can be converted to Top down but in that case we would need to make a 3D array that of dimension l*m*n so the recursive approach is more efficient and similar. So Skipping the Top Down approach