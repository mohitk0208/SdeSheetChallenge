'''
############## Minimum number of platforms required for railway ############
Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.

Your Task:
You don't need to read input or print anything. Your task is to complete the function findPlatform() which takes the array arr[] (denoting the arrival times), array dep[] (denoting the departure times) and the size of the array as inputs and returns the minimum number of platforms required at the railway station such that no train waits.

Note: Time intervals are in the 24-hour format(HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this may be > 59).

Input: n = 6
arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
Output: 3
Explanation:
Minimum 3 platforms are required to
safely arrive and depart all trains.

gfg : https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#

'''


# solution
# approach 1 : greedy
from heapq import heapify, heappush, heappop

class Solution:
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n ,arr ,dep):

        platforms = []                # it contains when a specific platform becomes free
        heappush(platforms, 0)        # create min heap

        trains = list(zip(arr, dep))  # sort the trains according to arrival time
        trains.sort()
        for a, d in trains:
            x = heappop(platforms)    # choose the platform which gets freed earliest
            if x < a:
                heappush(platforms, d)   # if train can come to the platform then update the free time
            else:
                heappush(platforms, x)     # else
                heappush(platforms, d)     # create add a new platform

        return len(platforms)   # return length of platforms