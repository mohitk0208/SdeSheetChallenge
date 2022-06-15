'''
############################### Count Inversions ###############################

For a given integer array/list 'ARR' of size 'N' containing all distinct values, find the total number of 'Inversions' that may exist.
An inversion is defined for a pair of integers in the array/list when the following two conditions are met.
A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:

1. 'ARR[i] > 'ARR[j]'
2. 'i' < 'j'

Where 'i' and 'j' denote the indices ranging from [0, 'N').

codestudio : https://www.codingninjas.com/codestudio/problems/count-inversions_615?leftPanelTab=0

'''

# solution approach 1: brute force
#    count the number of inversions in the array using two nested loops
def getInversions(arr, n) :
    count = [0]*n

    for i in range(n-1):
        for j in range(i+1, n ):
            if arr[i] > arr[j]:
                count[i] += 1


    return sum(count)