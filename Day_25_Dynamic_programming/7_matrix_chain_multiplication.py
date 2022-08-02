'''
##################### Matrix chain Multiplication ######################
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications.

The dimensions of the matrices are given in an array arr[] of size N (such that N = number of matrices + 1) where the ith matrix has the dimensions (arr[i-1] x arr[i]).

Input: N = 5
arr = {40, 20, 30, 10, 30}
Output: 26000
Explaination: There are 4 matrices of dimension
40x20, 20x30, 30x10, 10x30. Say the matrices are
named as A, B, C, D. Out of all possible combinations,
the most efficient way is (A*(B*C))*D.
The number of operations are -
20*30*10 + 40*20*10 + 40*10*30 = 26000.


gfg : https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

'''

# THIS IS A PROBLEM OF PARTITIONING DP


# solution

# approach 1 : recursive
class Solution:
    def matrixMultiplication(self, N, arr):

        matrix = [[-1]*N for _ in range(N)]

        def dp(i,j):
            if i == j:
                return 0

            if matrix[i][j] != -1:
                return matrix[i][j]

            min_ = float("inf")
            for k in range(i, j):
                val = arr[i-1]*arr[k]*arr[j] + dp(i, k) + dp(k+1, j)

                min_ = min(min_, val)


            matrix[i][j] = min_


            return min_


        return dp(1, N-1)
