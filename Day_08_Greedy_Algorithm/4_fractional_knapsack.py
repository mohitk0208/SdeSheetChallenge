'''
###################### Fractional Knapsack #############################
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item.
Your Task :
Complete the function fractionalKnapsack() that receives maximum capacity , array of structure/class and size n and returns a double value representing the maximum value in knapsack.
Note: The details of structure/class is defined in the comments above the given function.

Example 1:

Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.00
Explanation:Total maximum value of item
we can have is 240.00 from the given
capacity of sack.

gfg : https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1#

'''


# solution
# approach : greedy
#     - sort the items by value/weight ratio
#     - iterate over the sorted items
#     - if the weight of the item is less than the capacity of sack then add complete item to sack and update the capacity and value
#     - else, add the fractional part of the item to sack and update the capacity and value, exit the loop as no space left in the sack
#     - return the value of the sack
# SC -> O(1) and TC -> O(nlogn)
class Solution:
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,Items,n):
        Items.sort(key = lambda i: i.value / i.weight, reverse=True) # O(nlogn) # sort the items by value/weight ratio
        max_ = 0
        for x in Items: # O(n) # iterate over the sorted items
            if x.weight < W:
                max_ += x.value
                W -= x.weight

            else:
                max_ += (x.value/x.weight) * W
                break

        return max_

