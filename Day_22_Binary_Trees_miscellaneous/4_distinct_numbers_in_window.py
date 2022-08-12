'''
################## Distinct Numbers in Window #################
You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.

Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

NOTE:  if B > N, return an empty array.


interviewbit : https://www.interviewbit.com/problems/distinct-numbers-in-window/

'''


# solution
# approach 1: using hashmap(dict)
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        d = {}

        if B > len(A):
            return []

        ans = []

        i = 0

        while i < B:
            d[A[i]] = d.get(A[i], 0) + 1

            i += 1

        ans.append(len(d))

        while i < len(A):
            if d[A[i-B]] == 1:
                del d[A[i-B]]
            else:
                d[A[i-B]] -= 1

            d[A[i]] = d.get(A[i], 0) + 1

            ans.append(len(d))
            i+=1

        return ans

