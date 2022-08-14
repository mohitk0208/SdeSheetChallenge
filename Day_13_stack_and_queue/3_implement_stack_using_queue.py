'''
##################### Implement stack using queue #####################
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

- void push(int x) Pushes element x to the top of the stack.
- int pop() Removes the element on the top of the stack and returns it.
- int top() Returns the element on the top of the stack.
- boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.


leetcode : https://leetcode.com/problems/implement-stack-using-queues/

'''

# solution
# approach 1 : using one queues
from queue import Queue

class MyStack:

    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

        for _ in range(len(self.q.queue)-1):
            self.q.put(self.q.get())


    def pop(self) -> int:
        return self.q.get()

    def top(self) -> int:
        return self.q.queue[0]

    def empty(self) -> bool:
        return len(self.q.queue) == 0