'''
############### Flatten Binary Tree to Linked List #############
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


leetcode : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

'''


# solution
# approach 1 : recursive
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def traversal(node):
            if node == None:
                return None

            if node.left == None and node.right == None:
                return node

            if node.left == None:
                return traversal(node.right)

            if node.right == None:
                node.right = node.left
                node.left = None
                return traversal(node.right)


            left = node.left
            right = node.right

            node1 = traversal(node.left)
            node2 = traversal(node.right)



            node.left = None
            node.right = left
            node1.right = right

            return node2

        traversal(root)