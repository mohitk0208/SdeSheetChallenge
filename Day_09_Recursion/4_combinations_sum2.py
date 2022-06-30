'''
######################### Combinations Sum 2 #########################
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

leetcode : https://leetcode.com/problems/combination-sum-ii/

'''

# solution

# approach : trying most of the combinations
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        ans = set([])



        def combinations(arr, curr_arr, curr, sum_):

            if sum_ == target:
                ans.add(tuple(curr_arr))
                return

            if curr == len(arr) or sum_ > target:
                return

            combinations(arr, curr_arr+[arr[curr]], curr + 1, sum_+ arr[curr])
            combinations(arr, curr_arr, curr+1, sum_)


        combinations(candidates, [], 0, 0)

        return ans



# approach : trying combinations smartly
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()                             # sort the candidates so when we can end recursion when sum_ increases
        ans = set([])

        def combinations(arr, curr_arr, curr, t):
            if t == 0:
                ans.add(tuple(curr_arr))            # if target is 0 then add the combination to the set

            if curr >= len(arr) or arr[curr] > t:   # if curr is out of bounds or sum_ is greater than target then end further recursion calls
                return

            combinations(arr, curr_arr+[arr[curr]], curr+1, t-arr[curr]) # when curr is choosen decrease the required target
            x = curr + 1
            c = arr[curr]
            while x < len(arr):
                while x < len(arr) and arr[x] == c:
                    x += 1

                if x < len(arr):
                    if arr[x] <= t:
                        combinations(arr, curr_arr+[arr[x]], x+1, t-arr[x]) # call combinations for next different element
                    else:
                        break
                else:
                    break

                c = arr[x]

        combinations(candidates, [], 0, target)


        return ans
