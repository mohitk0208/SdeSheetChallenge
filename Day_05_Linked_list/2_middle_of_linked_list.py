'''
#################### Middle of Linked List ####################
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


leetcode : https://leetcode.com/problems/middle-of-the-linked-list/

'''

# solution
# SC -> O(1) and TC -> O(n)
# approach : use two pointers, one fast and one slow
#            fast pointer moves 2 steps at a time
#            slow pointer moves 1 step at a time
#            when fast pointer reaches the end, slow pointer will be at the middle
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head


        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next


        return slow