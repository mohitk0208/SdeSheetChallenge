'''
##################### Postorder Traversal ###################
Given the root of a binary tree, return the postorder traversal of its nodes' values.

leetcode : https://leetcode.com/problems/binary-tree-postorder-traversal/
'''


# solution
# approach 1 : recursive
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        l = []

        def postorder(r):
            if r == None:
                return

            postorder(r.left)
            postorder(r.right)
            l.append(r.val)


        postorder(root)