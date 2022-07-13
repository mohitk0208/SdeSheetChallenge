'''
####################### Merge K Sorted Arrays #############################
You have been given ‘K’ different arrays/lists, which are sorted individually (in ascending order). You need to merge all the given arrays/list such that the output array/list should be sorted in ascending order.



codestudio : https://www.codingninjas.com/codestudio/problems/merge-k-sorted-arrays_975379?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

'''



# solution
from heapq import *

def mergeKSortedArrays(kArrays, k:int):
    l = []

    for arr in kArrays:
        for x in arr:
            heappush(l, x)            # insert all values in the list l

    res = []

    for _ in range(len(l)):
        res.append(heappop(l))        # pop all values from the list l and append to the list res as the popped values are in sorted order

    return res