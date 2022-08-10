'''
################### Convert Binary tree to its mirror ##################
Given a Binary Tree, convert it into its mirror.

gfg : https://practice.geeksforgeeks.org/problems/mirror-tree/1

'''


# solution
# approach : recursive
class Solution:

    def mirror(self,root):

        def traversal(node):
            if node == None:
                return None

            traversal(node.left)
            traversal(node.right)

            node.left, node.right = node.right, node.left


        traversal(root)