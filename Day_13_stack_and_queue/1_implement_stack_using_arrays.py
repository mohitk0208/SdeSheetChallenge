'''
##################### Implement stack using arrays #################
Stack is a data structure that follows the LIFO (Last in First out) principle. Design and implement a stack to implement the following functions:

1. Push(num): Push the given number in the stack if the stack is not full.
2. Pop: Remove and print the top element from the stack if present, else print -1.
3. Top: Print the top element of the stack if present, else print -1.
4. isEmpty: Print 1 if the stack is empty, else print 0.
5. isFull: Print 1 if the stack is full, else print 0.

codestudio : https://www.codingninjas.com/codestudio/problems/stack-implementation-using-array_3210209?topList=striver-sde-sheet-problems&leftPanelTab=0

'''


# solution
# Stack class.
class Stack:

    def __init__(self, capacity: int):
        self.stack = [-1]*capacity
        self.capacity = capacity
        self.size = 0

    def push(self, num: int) -> None:
        if self.size < self.capacity:
            self.stack[self.size] = num
            self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        self.size -= 1
        return self.stack[self.size]

    def top(self) -> int:
        if self.size == 0:
            return -1
        return self.stack[self.size-1]

    def isEmpty(self) -> int:
        return 1 if self.size == 0 else 0

    def isFull(self) -> int:
        return 1 if self.size == self.capacity else 0