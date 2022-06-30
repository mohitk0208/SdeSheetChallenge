'''
###################### Job Sequencing  ######################
Given a set of N jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.

Example 1:

Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).

gfg : https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#

'''

# solution
# approach : greedy
#      - always pick the job with highest profit
#      - place it in the last slot, if it full check for second last, then third last and so on till we have an empty slot
#      - if no empty slot, move to next job
#      - repeat the steps
# SC -> O(n) and TC -> nlog(n)
class Solution:

    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs,n):

        jobs.sort(key=lambda x:x.profit, reverse =True) # sort the jobs in descending order of profit
        s = {}                                      # store the jobs in a dictionary
        count = 0                                   # count the number of jobs done
        total = 0                                   # total profit

        for job in jobs:
            id_, deadline, profit = job.id, job.deadline, job.profit
            if deadline > 0 and  deadline not in s:  # pick the job with highest profit and place in last slot
                total += profit
                count += 1
                s[deadline] = id_

            else:                                   # it last slot not available
                temp = deadline
                while deadline > 0 and deadline in s:# then check for second last, third last and so on till we have an empty slot
                    deadline -= 1

                if deadline != 0:                 # if found an empty slot then place the job in that slot
                    s[deadline] = id_
                    count += 1
                    total += profit

        return [count, total] # return the number of jobs done and the maximum profit