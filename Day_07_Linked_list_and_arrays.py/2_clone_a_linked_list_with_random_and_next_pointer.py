'''
############### Clone a linked list with random and next pointer ###############
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

leetcode : https://leetcode.com/problems/copy-list-with-random-pointer/


'''

# solution
# approach :
# 1. create a new node for each node in the original list
# 2. store the new node in a dictionary with the original node as key and the new node as value
# 3. set the next and random pointer of the new node to the new node in the dictionary
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        c = {}

        temp = head

        while temp != None:                     # 1. create a new node for each node in the original list
            x = Node(temp.val)
            c[temp] = x                         # 2. store the new node in a dictionary with the original node as key and the new node as value

            temp = temp.next


        temp = head
        res = Node(0)
        cur = res

        while temp != None:
            cur.next = c[temp]
            # 3. set the next and random pointer of the new node to the new node in the dictionary
            cur.next.next = c[temp.next] if temp.next != None else None
            cur.next.random = c[temp.random] if temp.random != None else None

            cur = cur.next
            temp = temp.next

        return res.next                        # 4. return the head of the copied linked list

