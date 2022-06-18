'''
#################### Remove Nth Node From End of Linked List ####################
Given the head of a linked list, remove the nth node from the end of the list and return its head.

leetcode : https://leetcode.com/problems/remove-nth-node-from-end-of-list/

'''

# solution
# SC -> O(1) and TC -> O(n)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None:
            return head

        if n == 0:
            return head

        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        if fast == None:
            slow = head.next
            return slow

        while fast.next != None:
            slow = slow.next
            fast = fast.next


        slow.next = slow.next.next

        return head