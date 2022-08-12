'''
################## Find median in stream of numbers ###############
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
# approach 1: using insort from bisect library
from bisect import insort

class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        insort(self.l, num)

    def findMedian(self) -> float:
        n = len(self.l)

        if n % 2 == 0:
            x = n // 2
            return (self.l[x] + self.l[x-1]) / 2

        else:
            return self.l[n // 2]




# approach 2 : using min_heap and max_heap
from heapq import heapify, heappop, heappush

class MedianFinder:

    def __init__(self):
        self.max_h = []       # stores the left half of the provided list
        self.min_h = []       # stored the right half of the provided list

    def addNum(self, num: int) -> None:
        l_max = len(self.max_h)
        l_min = len(self.min_h)

        if l_max == 0 and l_min == 0:
            heappush(self.max_h, -num)
            return

        if l_max > l_min:
            if num <= -self.max_h[0]:     # num needs to be inserted in left half
                heappush(self.max_h, -num)
                heappush(self.min_h, -heappop(self.max_h))
            else:
                heappush(self.min_h, num)
        else:
            if num > -self.max_h[0]:    # num needs to be inserted in right half
                heappush(self.min_h, num)
                heappush(self.max_h, -heappop(self.min_h))
            else:
                heappush(self.max_h, -num)


    def findMedian(self) -> float:
        l_max = len(self.max_h)
        l_min = len(self.min_h)

        if l_max == l_min:            # if equal elements in both list then
            return (-self.max_h[0] + self.min_h[0]) / 2  # median is average of largest of left half and smallest of right half
        else:
            return -self.max_h[0]