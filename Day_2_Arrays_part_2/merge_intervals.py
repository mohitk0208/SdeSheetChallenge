'''
######################## Merge Intervals ########################

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

leetcode : https://leetcode.com/problems/merge-intervals/

'''

#leetcode solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key= lambda x:x[0])        # sort by start

        res = []
        for i in range(len(intervals)):
            if len(res) == 0:
                res.append(intervals[i])
                continue

            if res[-1][1] >= intervals[i][0]:       # check if intervals overlap
                res[-1][0] = min(res[-1][0], intervals[i][0])   # update start
                res[-1][1] = max(res[-1][1], intervals[i][1])   # update end

            else:
                res.append(intervals[i])        # if does'nt overlap, add to res

        return res