'''
################ Flattening A linked List #################
Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order.
Note: The flattened list will be printed using the bottom pointer instead of next pointer.

Your Task:
You do not need to read input or print anything. Complete the function flatten() that takes the head of the linked list as input parameter and returns the head of flattened link list.


gfg : https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1#


'''

# solution
# approach 1: using extra space and merge sort concepts
# SC -> O(n) and TC -> O(n*n*m)

'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

'''
def merge(l1 , l2):                         # merge two sorted linked list and return head of merged list
    dummy = Node(0)
    dd = dummy

    while l1 != None and l2 != None:
        if l1.data <= l2.data:
            temp = Node(l1.data)
            dd.bottom = temp
            dd = dd.bottom
            l1 = l1.bottom
        else:
            temp = Node(l2.data)
            dd.bottom = temp
            dd = dd.bottom
            l2 = l2.bottom

    while l1 != None:
        temp = Node(l1.data)
        dd.bottom = temp
        dd = dd.bottom
        l1 = l1.bottom


    while l2 != None:
        temp = Node(l2.data)
        dd.bottom = temp
        dd = dd.bottom
        l2 = l2.bottom

    return dummy.bottom

def flatten(root):
    #Your code here
    if root == None or root.next == None:
        return root

    d = root.next.next                        # select thrid node in next

    f = root                                  # select first node in next
    s = root.next                             # select second node in next
    f.next = None                             # disconnect first and second node

    h = merge(f, s)                           # merge first and second
    while d != None:
        f = h
        s = d
        d = d.next
        s.next = None
        h = merge(f, s)

    return h


# approach : change merge function to use constant space
def merge(x1, x2):
    l1 = None
    l2 = None

    if x1.data <= x2.data:
        l1 = x1
        l2 = x2
    else:
        l1 = x2
        l2 = x1

    res = Node(0)
    res.bottom = l1
    pre = res

    while l1 != None and l2 != None:
        if l1.data <= l2.data:
            pre = l1
            l1 = l1.bottom
        else:
            temp = l2
            l2 = l2.bottom
            temp.bottom = l1
            pre.bottom = temp
            pre = temp

    if l2 != None:
        pre.bottom = l2


    return res.bottom


def flatten(root):
    if root == None or root.next == None:
        return root

    d = root.next.next

    f = root
    s = root.next
    f.next = None

    h = merge(f, s)
    while d != None:
        f = h
        s = d
        d = d.next
        s.next = None
        h = merge(f, s)

    return h
