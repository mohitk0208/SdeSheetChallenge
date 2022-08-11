'''
############### Check if BT is BST or not ###################
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


leetcode : https://leetcode.com/problems/validate-binary-search-tree/

'''


# solution
# approach 1 : recursive inorder traversal
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ino = []

        def inorder(node):
            if node == None:
                return

            inorder(node.left)
            ino.append(node.val)
            inorder(node.right)


        inorder(root)

        # Since inorder traversal of BST gives us a sorted array so verifying if the
        # inorder is sorted or not
        for i in range(1, len(ino)):
            if ino[i-1] >= ino[i]:  # if not then return False
                return False

        return True # else the BT is BST





# approach 2 : using single traversal
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(node, low, high):
            if node == None:
                return True

            if not (low < node.val < high):
                return False

            return check(node.left, low, node.val) and check(node.right, node.val, high)

        return check(root, float("-inf"), float("inf"))