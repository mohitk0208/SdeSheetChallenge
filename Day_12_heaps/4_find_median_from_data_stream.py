'''
##################### Find median from data stream #####################
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


leetcode : https://leetcode.com/problems/find-median-from-data-stream/

'''


# solution
# approach : using insort from bisect library
# -> this function inserts data in sorted form, so the data always remains sorted in list and hence the median is always the middle value
from bisect import insort

class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        insort(self.l, num)                 # insert Data in sorted form

    def findMedian(self) -> float:
        n = len(self.l)

        if n % 2 == 0:
            x = n // 2
            return (self.l[x] + self.l[x-1]) / 2

        else:
            return self.l[n // 2]





# approach : using heap
