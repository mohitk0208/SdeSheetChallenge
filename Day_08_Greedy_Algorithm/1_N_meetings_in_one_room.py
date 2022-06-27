'''
################# N meetings in one room #######################
There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

Your Task :
You don't need to read inputs or print anything. Complete the function maxMeetings() that takes two arrays start[] and end[] along with their size N as input parameters and returns the maximum number of meetings that can be held in the meeting room.

N = 6
start[] = {1,3,0,5,8,5}
end[] =  {2,4,6,7,9,9}
Output:
4
Explanation:
Maximum four meetings can be held with
given start and end timings.
The meetings are - (1, 2),(3, 4), (5,7) and (8,9)


gfg : https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#

'''


# solution
# SC -> O(n) and TC -> O(nlogn)
class Solution:

    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        meetings = list(zip(start, end))

        meetings.sort(key= lambda x:x[1])
        ans = 0
        limit = 0

        for s, e in meetings:
            if s > limit:
                # ans.append((s,e))
                ans += 1
                limit = e

        return ans