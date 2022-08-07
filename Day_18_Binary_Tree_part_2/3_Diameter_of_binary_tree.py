'''
##################### Diameter of Binary Tree #################
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


leetcode : https://leetcode.com/problems/diameter-of-binary-tree/

'''

# solution
# approach 1 : recursive (postorder traversal)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def length(node):
            if node == None:
                return -1

            l = length(node.left)
            r = length(node.right)
            temp =  l + r + 2
            self.ans = max(self.ans, temp)

            return max(l, r) + 1

        length(root)

        return self.ans