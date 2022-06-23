'''
############################## Detect cycle in Linked List ##############################
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

leetcode : https://leetcode.com/problems/linked-list-cycle/

'''


# solution
# approach : using tortoise and hare algorithm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None :
            return False

        slow = head                                                  # start from head
        fast = head

        while slow != None and fast != None and fast.next != None:  # if any of them becomes None , then there is no cycle
            slow = slow.next                                        # slow moves 1 step
            fast = fast.next.next                                   # fast moves 2 steps

            if slow == fast:                                        # if they collide , then there is a cycle
                return True

        return False