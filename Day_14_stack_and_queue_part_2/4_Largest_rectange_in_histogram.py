'''
##################### Largest Rectangle in Histogram #####################
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

leetcode : https://leetcode.com/problems/largest-rectangle-in-histogram/

'''



# solution
# approach 1: using stack
#   -> find nsl (Nearest Smaller Left) , store -1 if no smaller left
#   -> find nsr (Nearest Smaller Right) store len(heights) if no smaller right
#   -> find area (height * (nsr - nsl -1))
#   -> return the maximum area

# SC -> O(2n)  and TC -> O(n) + O(n) + O(n)
class Solution:
    def largestRectangleArea(self, heights) :
      #---------------- find NSL ----------------
        nsl = []
        stack = []

        for i in range(len(heights)):
            if len(stack) == 0:
                nsl.append(-1)

            elif stack[-1][0] < heights[i]:
                nsl.append(stack[-1][1])

            else:
                while len(stack) > 0 and stack[-1][0] >= heights[i]:
                    stack.pop()

                if len(stack) == 0:
                    nsl.append(-1)
                else:
                    nsl.append(stack[-1][1])

            stack.append((heights[i], i))

      #---------------- find NSR ----------------
        nsr = []
        stack = []

        for i in range(len(heights)-1,-1, -1 ):
            if len(stack) == 0:
                nsr.append(len(heights))

            elif stack[-1][0] < heights[i]:
                nsr.append(stack[-1][1])

            else:
                while len(stack) > 0 and stack[-1][0] >= heights[i]:
                    stack.pop()

                if len(stack) == 0:
                    nsr.append(len(heights))
                else:
                    nsr.append(stack[-1][1])


            stack.append((heights[i], i))

        nsr.reverse()

        #---------------- find area for each bar and choose the maximum ----------------

        max_ = 0
        for i, h in enumerate(heights):
            diff = nsr[i] - nsl[i] - 1
            max_ = max(max_, h*diff)

        return max_

