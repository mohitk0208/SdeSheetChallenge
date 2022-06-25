'''
######################### Reverse Nodes in K groups ##########################
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]


leetcode : https://leetcode.com/problems/reverse-nodes-in-k-group/

'''

# solution is complicated to understand, so do a try run

# solution
# SC -> O(1) and TC -> O(n)
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 1:
            return head

        dummy = ListNode()
        dummy.next = head

        cur, pre, nex = dummy, dummy, dummy

        count = 0

        while cur.next != None:
            cur = cur.next
            count += 1

        while count >= k:
            cur = pre.next
            nex = cur.next

            for _ in range(k-1):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next

            pre = cur
            count -= k

        return dummy.next