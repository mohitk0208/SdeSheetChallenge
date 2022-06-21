'''
################ Merge two sorted linked lists ################
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

leetcode : https://leetcode.com/problems/merge-two-sorted-lists/

'''


# solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 == None:
            return None

        if list1 == None:
            return list2

        if list2 == None:
            return list1


        ans = None
        anshead = None
        while list1 != None and list2 != None:

            if list1.val <= list2.val:
                if anshead == None:
                    ans = list1
                    anshead = ans
                    list1 = list1.next
                    ans.next = None
                else:
                    ans.next = list1
                    list1 = list1.next
                    ans.next.next = None
                    ans = ans.next

            else:
                if anshead == None:
                    ans = list2
                    anshead = ans
                    list2 = list2.next
                    ans.next = None
                else:
                    ans.next = list2
                    list2 = list2.next
                    ans.next.next = None
                    ans = ans.next

        if list1 != None:
            ans.next = list1

        if list2 != None:
            ans.next = list2

        return anshead