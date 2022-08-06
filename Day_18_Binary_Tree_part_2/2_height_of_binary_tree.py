'''
############### Height of Binary Tree #################
############### Depth of Binary Tree #################
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

leetcode : https://leetcode.com/problems/maximum-depth-of-binary-tree/


'''

# solution
# approach 1: recursive
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))