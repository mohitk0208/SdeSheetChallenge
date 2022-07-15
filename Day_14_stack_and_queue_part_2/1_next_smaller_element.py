'''
########################## Next Smaller Element ##########################
Given an array, find the nearest smaller element G[i] for every element A[i] in the array such that the element has an index smaller than i.

More formally,

    G[i] for an element A[i] = an element A[j] such that
    j is maximum possible AND
    j < i AND
    A[j] < A[i]
Elements for which no smaller element exist, consider next smaller element as -1.


interviewbit : https://www.interviewbit.com/problems/nearest-smaller-element/

'''

# solution
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        nsl = []

        stack = []

        for x in A:
            if len(stack) == 0:
                nsl.append(-1)

            elif stack[-1] < x:
                nsl.append(stack[-1])
            else:
                while len(stack) > 0 and stack[-1] >= x:
                    stack.pop()

                if len(stack) == 0:
                    nsl.append(-1)
                else:
                    nsl.append(stack[-1])

            stack.append(x)

        return nsl