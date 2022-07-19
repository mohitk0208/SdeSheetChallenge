'''
###################### Implement Min Stack ######################
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.


leetcode : https://leetcode.com/problems/min-stack/

'''


# solution
# SC -> O(2n)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    # TC -> O(1)
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)

    # TC -> O(1)
    def pop(self) -> None:
        if self.min[-1] == self.stack[-1]:
            self.min.pop()

        self.stack.pop()

    # TC -> O(1)
    def top(self) -> int:
        return self.stack[-1]

    # TC -> O(1)
    def getMin(self) -> int:
        return self.min[-1]