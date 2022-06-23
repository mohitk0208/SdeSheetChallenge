'''
############################ Find intersection point of y linked list ############################
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.


leetcode : https://leetcode.com/problems/intersection-of-two-linked-lists/

'''


# solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# approach 1 : brute force
# Sc -> O(1) and  TC -> O(m*n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        while headA != None:
            tempB = headB

            while tempB != None:
                if headA == tempB:
                    return headA

                tempB = tempB.next

            headA = headA.next

        return None




# approach 2 : using hash table
# SC -> O(n) and TC -> O(m+n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        c = set([])

        while headA != None:
            c.add(headA)
            headA = headA.next

        while headB != None:
            if headB in c:
                return headB

            headB = headB.next

        return None



# approach 3 : length difference
# SC -> O(1) and  TC -> O(m+n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        len1 = 0
        len2 = 0

        tempA = headA
        while tempA != None:
            len1 += 1
            tempA = tempA.next

        tempB = headB
        while tempB != None:
            len2 += 1
            tempB = tempB.next

        if len1 >= len2 :
            diff = len1 - len2

            for _ in range(diff):
                headA = headA.next

        else:
            diff = len2 - len1

            for _ in range(diff):
                headB = headB.next


        while headA != headB :
            headA = headA.next
            headB = headB.next

        return headA







# approach 3 : optimized length difference approach using two pointers
# SC -> O(1) and TC -> O(m+n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        temp1 = headA
        temp2 = headB

        while temp1 != temp2:
            if temp1 == None:
                temp1 = headB
                continue

            if temp2 == None:
                temp2 = headA
                continue

            temp1 = temp1.next
            temp2 = temp2.next

        return temp1

