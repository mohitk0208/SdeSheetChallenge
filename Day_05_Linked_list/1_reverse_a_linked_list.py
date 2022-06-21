'''
################### Reverse a linked list ###################
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


leetcode : https://leetcode.com/problems/reverse-linked-list/

'''

# solution
# SC -> O(1) and Tc -> O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head


        temp = None

        while head != None:
            curr = head
            head = head.next

            curr.next = temp
            temp = curr

        return temp