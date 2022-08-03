'''
########################## Coin Change ######################
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1


leetcode : https://leetcode.com/problems/coin-change/

'''


# solution

# approach 1 : using 2D array
# here every element of 2D array  arr[n][m] represent minimum number of coins needed to get an amount `m` using the
# first `n` coins only
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        t = [[amount+1]*(amount+1) for _ in range(n+1)]

        for i in range(1, n+1):
            t[i][0] = 0


        for i in range(1, n+1):
            for j in range(1, amount+1):
                if coins[i-1] <= amount:
                    t[i][j] = min(t[i-1][j], 1+t[i][j-coins[i-1]])
                else:
                    t[i][j] = t[i-1][j]

        if t[n][amount] >= (amount+1):
            return -1

        return t[n][amount]




# approach 2 : using 1D array (recursive)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dp(a):
            if a == 0:
                return 0

            min_ = float("inf")
            for coin in coins:
                if coin <= a :
                    min_ = min(min_, 1+ dp(a-coin))

            return min_

        val = dp(amount)

        return -1 if val == float("inf") else val




# approach 3 : 1D array Top down (Tabulation)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        a = [float("inf") for i in range(amount+1)]

        a[0] = 0

        coins.sort()

        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    a[i] = min(a[i], 1 + a[i-coin])
                else:
                    break

        return -1 if a[amount] == float("inf") else a[amount]