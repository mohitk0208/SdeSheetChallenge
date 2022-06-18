'''
############## Longest Consecutive Sequence ##############

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

leetcode : https://leetcode.com/problems/longest-consecutive-sequence/

'''


# solution
# approach 1 : sorting the array
# SC -> O(1) and TC -> O(N) + O(NlogN) + O(N) = O(NlogN)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = list(set(nums))        # remove duplicates
        nums.sort()                # sort the array
        max_ = 0                  # stores maximum consecutive sequence length
        curr = 0                  # stores current consecutive sequence length
        for i in range(len(nums)):

            if i == 0:            # if first element then curr = 1
                curr = 1
                continue

            if nums[i] == nums[i-1]+1:      # increment curr if consecutive
                curr += 1
            else:
                max_ = max(max_, curr)      # update max if curr is greater than max
                curr = 1                    # reset curr

        max_ = max(max_ , curr)

        return max_




# approach 2 : use set
# SC -> O(n) and TC -> O(n) + O(n) + O(n) = O(3n) = O(n)
#         - make a set
#         - iterate over each element and check if it exist in set or not
#         - if exist then move to next element
#         - if doesn't exist then start counting from current number till the sequence exist in the set
#         - update max if current count is greater than max_
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # using set
        # SC -> O(n) and TC -> O(n) + O(n) + O(n) = O(3n) = O(n)

        nums = set(nums)        # O(n)
        max_ = 0
        for x in nums:          # O(n)
            if x-1 in nums:     # O(1)
                continue

            count = 1
            while x + 1 in nums: # O(n)
                x +=1
                count += 1

            max_ = max(max_, count)

        return max_