'''
###################### Maximum Sum Combination ###############
You are given two arrays/lists ‘A’ and ‘B’ of size ‘N’ each. You are also given an integer ‘K’. You have to find the ‘K’ maximum and valid sum combinations from all the possible sum combinations of the arrays/lists ‘A’ and ‘B’.
Sum combination is made by adding one element from array ‘A’ and another element from array ‘B’.

For Example :
A : [1, 3]
B : [4, 2]
K : 2
The possible sum combinations can be 5(3 + 2), 7(3 + 4), 3(1 + 2), 5(1 + 4). The 2 maximum sum combinations are 7 and 5.

codestudio : https://www.codingninjas.com/codestudio/problems/k-max-sum-combinations_975322?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

'''


# solution
# approach : naive approach using heap
from heapq import heapify, heappush, heappop

def kMaxSumCombination(a, b, n, k):
    vals = []
    heapify(vals)

    for x in a:
        for y in b:
            heappush(vals, -(x+y))

    res = []
    for _ in range(k):
        res.append(heappop(vals)*-1)

    return res