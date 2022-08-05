'''
###################### Egg Dropping Problem #####################
You are given N identical eggs and you have access to a K-floored building from 1 to K.

There exists a floor f where 0 <= f <= K such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break. There are few rules given below.

An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If the egg doesn't break at a certain floor, it will not break at any floor below.
If the eggs breaks at a certain floor, it will break at any floor above.
Return the minimum number of moves that you need to determine with certainty what the value of f is.

For more description on this problem see wiki page


Example 1:

Input:
N = 1, K = 2
Output: 2
Explanation:
1. Drop the egg from floor 1. If it
   breaks, we know that f = 0.
2. Otherwise, drop the egg from floor 2.
   If it breaks, we know that f = 1.
3. If it does not break, then we know f = 2.
4. Hence, we need at minimum 2 moves to
   determine with certainty what the value of f is.



gfg : https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1


'''

# here the task is to find the minimum number of moves in the worst case to find the threshold floor(The floor after which the egg breaks)



# solution
# approach 1: recursive
class Solution:

    def eggDrop(self,n, k):

        matrix = [[-1]*(k+1) for _ in range(n+1)]


        def dp(e, f):

            if e == 1 or f == 0  or f == 1:
                return f


            if matrix[e][f] != -1:
                return matrix[e][f]

            min_ = float("inf")
            for k in range(1, f+1):
                val = 1 + max(dp(e-1, k-1), dp(e, f-k))

                min_ = min(min_, val)

            matrix[e][f] = min_

            return min_

        return dp(n, k)