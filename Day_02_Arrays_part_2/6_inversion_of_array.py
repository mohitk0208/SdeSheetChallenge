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
# SC -> O(1) and TC -> O(N^2)
#    count the number of inversions in the array using two nested loops
def getInversions(arr, n) :
    count = 0

    for i in range(n-1):
        for j in range(i+1, n ):
            if arr[i] > arr[j]:
                count += 1


    return count


# solution 2 : modified merge sort
#    count the number of inversions in the array using modified merge sort
# SC -> O(N) and TC -> O(NlogN)
def merge(arr, temp, left, mid, right):
    i, j = left, mid
    temp_idx = left
    inv_count = 0

    while i <= mid-1 and j <= right:
        if arr[i] <= arr[j]:
            temp[temp_idx] = arr[i]
            temp_idx += 1
            i += 1
        else:
            temp[temp_idx] = arr[j]
            temp_idx += 1
            j += 1
            inv_count += (mid - i)  # it means that all numbers in the right of i to the mid are greater than arr[j]
                                    # as the left half is sorted so `no. of inversions = inv_count + (mid - i)`

    while i <= mid -1 :
        temp[temp_idx] = arr[i]
        temp_idx += 1
        i += 1

    while j <= right:
        temp[temp_idx] = arr[j]
        temp_idx += 1
        j += 1

    i = left
    while i <= right:
        arr[i] = temp[i]
        i += 1

    return inv_count


def _mergesort(arr, temp, left, right):
    inv_count = 0

    if right > left:
        mid = (left + right) // 2

        inv_count += _mergesort(arr, temp, left, mid)           # count inversions in left half
        inv_count += _mergesort(arr, temp, mid+1, right)        # count inversions in right half

        inv_count += merge(arr, temp, left, mid+1, right)       # count inversions while merging

    return inv_count        # return the total number of inversions


def getInversions(arr, n) :
    temp = [0]*n

    return _mergesort(arr, temp, 0, n-1)
