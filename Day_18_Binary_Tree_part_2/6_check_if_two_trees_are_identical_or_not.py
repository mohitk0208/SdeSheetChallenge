'''
################### Check if two trees are identical or not ##############
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

leetcode : https://leetcode.com/problems/same-tree/

'''

# solution
# approach 1 : recursive
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True

        if p != None and q != None and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True

        return False