'''
################### Check if Binary Tree is Balanced or Not ################
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


leetcode : https://leetcode.com/problems/balanced-binary-tree/

'''


# solution
# approach 1 : postorder traversal
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.ans = True
        def traversal(node):
            if node == None:
                return 0

            if not self.ans :
                return 0

            l = traversal(node.left)
            r = traversal(node.right)

            if abs(l-r) > 1:
                self.ans = False

            return max(l, r) + 1

        traversal(root)

        return self.ans