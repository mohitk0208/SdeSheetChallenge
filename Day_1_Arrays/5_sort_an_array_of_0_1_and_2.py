'''

############################# Sort an array of 0, 1 and 2 #############################

You have been given an integer array/list(ARR) of size 'N'. It only contains 0s, 1s and 2s. Write a solution to sort this array/list.

leetcode : https://leetcode.com/problems/sort-colors/
codestudio : https://www.codingninjas.com/codestudio/problems/631055?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

'''


# leetcode solution
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0

        for x in nums:
            if x == 0:
                red += 1
            elif x == 1:
                white += 1
            else:
                blue += 1

        i = 0
        while i < red:
            nums[i] = 0
            i+=1

        while i < red+white:
            nums[i] = 1
            i+=1

        while i < red+white+blue:
            nums[i] = 2
            i+=1



# codestudio solution
    count = [0, 0 , 0 ]             # count 0's , 1's and 2's

    for x in arr:
        count[x] += 1

                                    # store 0's in the front
                                    # store 1's in the middle
                                    # store 2's in the end
    for i in range(len(arr)):
        if i < count[0]:
            arr[i] = 0
        elif i < count[0] + count[1]:
            arr[i] = 1
        else:
            arr[i] = 2
