'''
####################### Preorder Traversal #################
Given the root of a binary tree, return the preorder traversal of its nodes' values.

leetcode : https://leetcode.com/problems/binary-tree-preorder-traversal/

'''


# solution
# approach 1 : recursive
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        l = []

        def preorder(r):
            if r == None:
                return

            l.append(r.val)
            preorder(r.left)
            preorder(r.right)


        preorder(root)

        return l