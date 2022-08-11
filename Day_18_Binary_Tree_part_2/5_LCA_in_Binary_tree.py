'''
################## LCA in Binary Tree #################
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


leetcode : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

'''

# solution
# approach 1 : recursive
# SC -> O(1) and TC -> O(N)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(node):
            if node == None:
                return None

            if node == p or node == q:
                return node

            l = lca(node.left)
            r = lca(node.right)

            if l == None and r != None:
                return r
            elif l != None and r == None:
                return l
            elif l != None and r != None:
                return node

            return None

        return lca(root)
