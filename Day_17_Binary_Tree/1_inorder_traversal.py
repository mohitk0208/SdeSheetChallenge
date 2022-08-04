'''
#################### Inorder Traversal ##################
Given the root of a binary tree, return the inorder traversal of its nodes' values.


leetcode : https://leetcode.com/problems/binary-tree-inorder-traversal/

'''


# solution
# approach 1 : recursive
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        l = []

        def inorder(r):
            if r == None:
                return

            inorder(r.left)
            l.append(r.val)
            inorder(r.right)

        inorder(root)


        return l
