'''
######################## Check for Palindrome #########################
Given the head of a singly linked list, return true if it is a palindrome.
Example 1:
1->2->2->1
Input: head = [1,2,2,1]
Output: true

Example 2:
1->2
Input: head = [1,2]
Output: false


leetcode : https://leetcode.com/problems/palindrome-linked-list/

'''


# solution 1: Naive Approach
# SC -> O(n)  and TC -> O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = []

        while head != None:
            s.append(head.val)
            head = head.next

        return s == s[::-1]


# approach 2: optimized approach
# explanation:
#      1. find mid of the linked list
#      2. reverse the second half of the linked list
#      3. compare the first half and second half
#             - place a dummy pointer at the beginning of the first half
#             - place the slow pointer at the beginning of the second half
#             - increase both when their values are equal, if not equal return False
#             - if slow pointer becomes None, return True
#      4. if equal, return True
#      5. else, return False
# SC -> O(1)  and TC -> O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head == None or head.next == None:
            return True

# ----------------- Find the mid of the linked list -----------------
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

# ----------------- Reverse the second half of the linked list -----------------

        dummy = slow
        pre = dummy

        cur = pre.next
        nex = cur.next

        while cur.next != None:
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next

# ----------------- Compare the first half and second half -----------------

        fast = head
        slow = slow.next

        while slow.val == fast.val:
            slow = slow.next
            fast = fast.next

            if slow == None: # if slow pointer becomes None, return True
                return True

        return False # if not equal, return False