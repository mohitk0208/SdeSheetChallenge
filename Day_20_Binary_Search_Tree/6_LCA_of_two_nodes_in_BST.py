'''
################# LCA of two nodes in BST ##################
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


leetcode : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

'''


# solution
# approach 1 : recursive
# if p and q are both less than node then call lca() for node.left
# if p and q are both greater than node then call lca() for node.right
# else call lca on both node.left and node.right
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(node):
            if node == None:
                return None

            if node.val > p.val  and node.val > q.val:    #if p and q are both less than node then call lca() for node.left
                return lca(node.left)

            if node.val < p.val and node.val < q.val:   #if p and q are both greater than node then call lca() for node.right
                return lca(node.right)

            if node == p or node == q:    # if node is either p or q return return it
                return node

            l = lca(node.left)
            r = lca(node.right)

            if l != None and r == None:
                return l

            elif l == None and r != None:
                return r
            elif l != None and r != None:
                return node

            return None

        return lca(root)