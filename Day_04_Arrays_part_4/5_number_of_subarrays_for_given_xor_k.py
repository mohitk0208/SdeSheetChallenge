'''
################## number of subarray for given xor k ############
Given an array of integers A and an integer B.

Find the total number of subarrays having bitwise XOR of all elements equals to B.


interviewbit : https://www.interviewbit.com/problems/subarray-with-given-xor/

'''


# solution
# approach 1 : brute force
# Sc -> O(1) and TC -> O(N)
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        count = 0

        val = 0

        for i in range(len(A)):
            ans = 0
            for j in range(i, len(A)):
                ans = ans ^ A[j]

                if ans == B:
                    count += 1

        return count



# approach 2 : storing prefix xor frequency
# SC -> < O(N) and TC -> O(N) considering insertion in dict requires O(1) time complexity
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        prefix = 0
        d = {}
        count = 0

        for a in A:

            prefix = prefix^a
            if prefix == B:
                count += 1

            y = prefix ^ B
            count += d.get(y, 0)

            d[prefix] = d.get(prefix, 0) + 1

        return count