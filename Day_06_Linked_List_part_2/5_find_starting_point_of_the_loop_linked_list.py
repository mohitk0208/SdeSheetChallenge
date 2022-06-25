'''
########################### Find the starting point of the loop in the linked list #############################
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

leetcode : https://leetcode.com/problems/linked-list-cycle-ii/

'''

# solution :
# approach : tortoise and hare algorithm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None


        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if fast == None or fast.next == None:
            return None

        fast = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow