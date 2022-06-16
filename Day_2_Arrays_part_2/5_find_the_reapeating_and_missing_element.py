'''

############################## Find the repeating and missing element ##############################

You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.
Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3]
Output:[3, 4]

A = 3, B = 4


interviewbit : https://www.interviewbit.com/problems/repeat-and-missing-number-array
codestudio : https://www.codingninjas.com/codestudio/problems/873366?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

'''



# solution
# approach 1 : using extra memory (set data structure)
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):

        s = set([])
        repeat = None
        missing = None
        sum_ = 0
        for x in A:
            if repeat == None and x in s:
                repeat = x
            else:
                s.add(x)

            sum_ += x

        actual_sum = (len(A) * (len(A) + 1) ) // 2

        missing = actual_sum -  (sum_ - repeat)

        return [repeat, missing]


# approach 2 : without extra memory (using XOR)


