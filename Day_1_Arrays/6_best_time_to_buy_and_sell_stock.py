'''
########################### Best time to buy and sell stock ###########################

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

leetcode : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
codestudio : https://www.codingninjas.com/codestudio/problems/893405?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=1

'''

# leetcode solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_stack = [prices[0]]                   # contains nearest smaller to left NSR

        for i in range(1, len(prices)):
            min_stack.append(min(min_stack[-1], prices[i])) # add the nearest smaller to left NSR

        max_stack_r = [prices[-1]]                # contains nearest greater to right NGR
        for i in range(len(prices) - 2, -1, -1):
            max_stack_r.append(max(max_stack_r[-1], prices[i])) # add the nearest greater to right NGR

        max_stack_r.reverse()

        max_ = 0                            # if prices is in decreasing order then max_ will be 0
        for i in range(len(prices)):
            if min_stack[i] < max_stack_r[i]:         # find the max profit from the two stacks
                max_ = max(max_, max_stack_r[i] - min_stack[i])


        return max_


# codestudio solution
def maximumProfit(prices):
    min_stack = [prices[0]]

    for i in range(1, len(prices)):
        min_stack.append(min(min_stack[-1], prices[i]))

    max_stack_r = [prices[-1]]
    for i in range(len(prices) - 2, -1, -1):
        max_stack_r.append(max(max_stack_r[-1], prices[i]))

    max_stack_r.reverse()

    max_ = 0
    for i in range(len(prices)):
        if min_stack[i] < max_stack_r[i]:
            max_ = max(max_, max_stack_r[i] - min_stack[i])


    return max_