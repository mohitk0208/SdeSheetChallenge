'''
################### Combinations Sum 1 ###################
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

leetcode : https://leetcode.com/problems/combination-sum/

'''

# solution
# approach : recursive
# SC -> does not depend on n
# TC -> O(2^n)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()                 # sort the candidates so when we can end recursion when sum_ increases
        ans = set([])                     # target,  as adding more values will not help decrease the value of sum_

        def combinations(arr, curr_arr, curr, sum_):

            if sum_ == target:
                ans.add(tuple(curr_arr))      # add the combination to the set when sum_ is equal to target
                return

            if curr == len(arr) or sum_ > target: # if curr is out of bounds or sum_ is greater than target then end further recursion calls
                return

            combinations(arr, curr_arr+[arr[curr]], curr, sum_+ arr[curr]) # when curr is choosen
            combinations(arr, curr_arr, curr+1, sum_)                  # when curr is not choosen


        combinations(candidates, [], 0, 0)

        return ans