'''
#################### Top View of Binary Tree #####################
Given below is a binary tree. The task is to print the top view of binary tree. Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /   \
4    5  6   7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node.


gfg : https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1

'''

# solution
# approach 1: recursive (preorder traversal)
# any traversal will work
class Solution:

    def topView(self,root):
        d = {}

        def preorder(node, hd, level):
            if node == None:
                return

            if hd in d:
                if level < d[hd][1]:
                    d[hd] = (node.data, level)
            else:
                d[hd] = (node.data, level)

            preorder(node.left, hd-1, level+1)
            preorder(node.right, hd+1, level+1)

        preorder(root, 0, 0)

        ans = map(lambda x:x[1][0], sorted(d.items()) )

        return ans