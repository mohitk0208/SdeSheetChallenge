'''
######################## Rotate a Linked List ###################
Given the head of a linked list, rotate the list to the right by k places.
Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]


leetcode : https://leetcode.com/problems/rotate-list/

'''



# solution
# SC -> O(1) and TC -> O(n) + O(n)
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None or k == 0:
            return head
        l = 0                     # length of the list
        cur = head

        while cur != None:
            cur = cur.next
            l += 1

        r = k % l                 # rotation to perform

        slow = head
        fast = head

        for _ in range(r):
            fast = fast.next      # increase fast by r steps

        while fast.next != None:    # till fast reaches the last node
            slow = slow.next
            fast = fast.next

        # Rotation takes place
        fast.next = head
        head = slow.next
        slow.next = None

        return head       # return the new head