'''
################ Add two numbers as linked list ################
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

leetcode : https://leetcode.com/problems/add-two-numbers/

'''


# solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            return None

        if l1 == None:
            return l2

        if l2 == None:
            return l1

        ans = ListNode()                      # head of the answer linked list
        curr = ans                            # curr to point to the current digit in the answer linked list

        # --------------- Add the first digit of both numbers  ---------------
        carry = 0
        curr.val = (l1.val + l2.val) % 10
        carry = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next

        # --------------- Add the rest of the digits  ---------------
        while l1 != None and l2 != None:
            sum_ = l1.val + l2.val + carry
            temp = ListNode(sum_ % 10)
            carry = sum_ // 10

            curr.next = temp
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        # --------------- Add the rest of the digits of l1  ---------------
        while l1 != None:
            sum_ = l1.val + carry
            temp = ListNode(sum_ % 10)
            carry = sum_ // 10

            curr.next = temp
            curr = curr.next
            l1 = l1.next

        # --------------- Add the rest of the digits of l2  ---------------
        while l2 != None:
            sum_ = l2.val + carry
            temp = ListNode(sum_ % 10)
            carry = sum_ // 10

            curr.next = temp
            curr = curr.next
            l2 = l2.next

        # --------------- Add the carry (if any)  ---------------
        if carry != 0:
            temp = ListNode(carry)
            curr.next = temp
            curr = curr.next

        return ans                           # return the head of the answer linked list