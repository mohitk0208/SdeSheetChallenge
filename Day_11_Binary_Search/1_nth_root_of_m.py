'''
######################### Nth root of M (use binary search) #########################
You are given two positive integers N and M. You have to find the Nth root of M i.e. M^(1/N).
Sample Input 1:
1
3 27
Sample Output 1:
3.000000


codestudio : https://www.codingninjas.com/codestudio/problems/1062679?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

'''



# I don't know why, but it gives runtime error in codestudio

# solution
# approach : Binary Search
import math

def findNthRootOfM(n,m):

    low = 0
    high = m
    accuracy = 10**(-7)
    mid = 0
    while high - low > accuracy:          # check if the answer id correct till 6 decimal places
        mid = (low + high) / 2.0          # find the mid point
        mid = float("{0:.10f}".format(mid))


        v = math.pow(mid, n)              # find the value of mid^n
        if v > m:                         # if the value is greater than m, then mid is too high
            high = mid                    # so answer's range becomes low - mid
        else:
            low = mid                     # answer's range becomes mid - high

    return "{0:.6f}".format(mid)          # format the answer to 6 decimal places